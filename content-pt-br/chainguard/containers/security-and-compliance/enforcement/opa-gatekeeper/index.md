---
title: "Aplicação de políticas no Kubernetes com o OPA Gatekeeper"
linktitle: "OPA Gatekeeper"
type: "article"
description: "Como aplicar boas práticas e garantir a conformidade com o OPA Gatekeeper."
date: 2025-09-02T10:00:00-00:00
lastmod: 2026-10-01T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Overview", "Policy"]
images: []
weight: 20
toc: true
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

O [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) é um controlador de admissão que aplica políticas em clusters Kubernetes. Este artigo explica como usá-lo para garantir que os recursos sigam boas práticas relacionadas ao uso dos Chainguard Containers.

## Pré-requisitos

Para seguir os exemplos deste guia, você vai precisar de:

- `kubectl`, a ferramenta de linha de comando do Kubernetes, instalado na sua máquina local.
- Acesso administrativo a um cluster Kubernetes em que o [OPA Gatekeeper já esteja instalado](https://open-policy-agent.github.io/gatekeeper/website/docs/install).

## Garantir que as imagens sejam baixadas de repositórios permitidos

Você pode usar a [constraint `K8sAllowedReposV2`](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/allowedreposv2) da [Gatekeeper Library](https://github.com/open-policy-agent/gatekeeper-library) para garantir que as imagens sejam baixadas apenas de uma lista de repositórios permitidos.

Para configurar essa constraint, adicione o constraint template ao seu cluster.

```shell
kubectl create -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper-library/refs/heads/master/library/general/allowedreposv2/template.yaml
```

Em seguida, crie uma constraint que permita apenas imagens hospedadas em `cgr.dev`. Se você espelha as imagens de contêiner da Chainguard em outro registro, pode substituir esse valor pelas suas próprias URLs:

```shell
kubectl create -f - <<EOF
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sAllowedReposv2
metadata:
  name: repo-is-cgr-dev
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    excludedNamespaces:
      - "kube-system"
  parameters:
    allowedImages:
      - "cgr.dev/*"
EOF
```

Em algumas soluções gerenciadas de Kubernetes, talvez você não consiga controlar onde ficam hospedadas as imagens fornecidas pela plataforma.

Para testar se essa constraint está funcionando, tente criar um pod que não esteja em conformidade:

```shell
kubectl create -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx-disallowed
spec:
  containers:
    - name: nginx
      image: nginx
EOF
```

```output
Error from server (Forbidden): error when creating "STDIN": admission webhook "validation.gatekeeper.sh" denied the request: [repo-is-cgr-dev] container <nginx> has an invalid image <nginx>, allowed images are ["cgr.dev/*"]
```

Este exemplo tenta criar um pod usando uma imagem de contêiner baixada do registro Docker Hub, e não do registro da Chainguard. Como mostra a saída, a tentativa de criar um pod fora de conformidade resultou em um erro, e a solicitação foi negada.

## Garantir que as imagens sejam referenciadas por digest

Os Chainguard Containers são atualizados com frequência para incorporar correções de CVEs e atualizações de pacotes. As tags das imagens de contêiner da Chainguard são altamente mutáveis, ou seja, a imagem subjacente muda com frequência, mesmo em tags muito específicas, como `v1.2.3-r1`.

Para evitar que atualizações introduzam mudanças incompatíveis, você pode baixar as imagens por digest e assim garantir o uso de uma imagem específica.

A [constraint `K8sImageDigests`](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/imagedigests) da [Gatekeeper Library](https://github.com/open-policy-agent/gatekeeper-library) pode ser usada para exigir essa prática dentro de um cluster Kubernetes.

Adicione o template ao seu cluster:

```shell
kubectl create -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper-library/refs/heads/master/library/general/imagedigests/template.yaml
```

Em seguida, crie a constraint:

```shell
kubectl create -f - <<EOF
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sImageDigests
metadata:
  name: container-image-must-have-digest
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    excludedNamespaces:
      - "kube-system"
EOF
```

Em algumas soluções gerenciadas de Kubernetes, talvez você não consiga controlar se as imagens fornecidas pela plataforma são referenciadas por digest.

Para testar a constraint, tente criar um pod que não esteja em conformidade:

```shell
kubectl create -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx-disallowed
spec:
  containers:
    - name: nginx
      image: cgr.dev/chainguard/nginx
EOF
```

```output
Error from server (Forbidden): error when creating "STDIN": admission webhook "validation.gatekeeper.sh" denied the request: [container-image-must-have-digest] container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>
```

Este exemplo tenta criar um pod usando a imagem de contêiner `nginx` da Chainguard, mas não baixa a imagem pelo digest, como a constraint exige. Como mostra a saída, a tentativa resultou em um erro, e a solicitação foi negada.

## Avisar primeiro, bloquear depois

Ao introduzir novas constraints em um cluster, é uma boa ideia configurá-las inicialmente com [`enforcementAction: warn`](https://open-policy-agent.github.io/gatekeeper/website/docs/violations/#warn-enforcement-action) para não bloquear as cargas de trabalho existentes.

Assim, quando um usuário cria um recurso fora de conformidade, ele recebe um aviso como o do exemplo a seguir. Isso indica ao usuário que ele deve atualizar a configuração.

```output
Warning: [container-image-must-have-digest] container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>
```

Você também pode encontrar os recursos fora de conformidade que já existem no cluster consultando as violações da constraint:

```shell
kubectl get k8simagedigests container-image-must-have-digest -o json | jq -r '.status.violations[]'
```

```output
{
  "enforcementAction": "warn",
  "group": "",
  "kind": "Pod",
  "message": "container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>",
  "name": "nginx-disallowed",
  "namespace": "default",
  "version": "v1"
}
```

Depois de resolver todas as violações, você pode remover `enforcementAction: warn`, e o Gatekeeper passará a bloquear a criação de recursos que violem a constraint.

## Garantir que as imagens sejam assinadas pela Chainguard

Para isso, os dados externos (external data) do [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) precisam estar habilitados.

### Instalar o Ratify

```shell
helm repo add ratify https://notaryproject.github.io/ratify
# download the notary verification certificate
curl -sSLO https://raw.githubusercontent.com/deislabs/ratify/main/test/testdata/notation.crt
helm install ratify \
    ratify/ratify \
    --namespace gatekeeper-system \
    --set-file notationCerts={./notation.crt} \
    --set featureFlags.RATIFY_CERT_ROTATION=true \
    --set policy.useRego=true
```

### Criar um verificador

O [verificador](https://ratify.dev/docs/reference/custom%20resources/verifiers) configura a verificação com o cosign. Este exemplo usa as imagens públicas da Chainguard.

> **Observação**: Se quiser usar um registro privado, siga os padrões de identidade descritos [para registros privados e dedicados](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/#privatededicated-registry).

```yaml
apiVersion: config.ratify.deislabs.io/v1beta1
kind: Verifier
metadata:
  name: verifier-cosign-chainguard
spec:
  name: cosign
  artifactTypes: application/vnd.dev.cosign.artifact.sig.v1+json
  parameters:
    trustPolicies:
      - name: chainguard-public
        scopes:
          - "cgr.dev/chainguard/*"
        tLogVerify: true
        keyless:
          ctLogVerify: true
          certificateOIDCIssuer: "https://token.actions.githubusercontent.com"
          certificateIdentity: "https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main"
```

Para usar um registro privado, são necessárias mais algumas etapas.

Primeiro, defina uma variável para a sua organização:

```shell
PARENT=your-organization
```

Em seguida, crie mais duas variáveis para guardar os UIDPs das identidades `catalog_syncer` e `apko_builder` da sua organização, respectivamente:

```shell
CATALOG_SYNCER=$(chainctl iam account-associations describe $PARENT -o json | jq -r '.[].chainguard.service_bindings.CATALOG_SYNCER')
APKO_BUILDER=$(chainctl iam account-associations describe $PARENT -o json | jq -r '.[].chainguard.service_bindings.APKO_BUILDER')
```

Depois, o seu verificador usaria essas variáveis em `certificateOIDCIssuer` e `certificateIdentityRegexp`. Substitua `${PARENT}`, `${CATALOG_SYNCER}` e `${APKO_BUILDER}` pelos valores literais.

```yaml
apiVersion: config.ratify.deislabs.io/v1beta1
kind: Verifier
metadata:
  name: verifier-cosign-chainguard
spec:
  name: cosign
  artifactTypes: application/vnd.dev.cosign.artifact.sig.v1+json
  parameters:
    trustPolicies:
      - name: chainguard-private
        scopes:
          - "cgr.dev/${PARENT}/*"
        tLogVerify: true
        keyless:
          ctLogVerify: true
          certificateOIDCIssuer: "https://issuer.enforce.dev"
          certificateIdentityRegExp: "https://issuer.enforce.dev/(${CATALOG_SYNCER}|${APKO_BUILDER})"
```

### Criar a política

Crie a [política](https://ratify.dev/docs/reference/custom%20resources/policies/#policy) do Ratify. Ela define como os resultados da verificação de um artefato são avaliados.

```yaml
apiVersion: config.ratify.deislabs.io/v1beta1
kind: Policy
metadata:
  name: ratify-policy
spec:
  type: config-policy
  parameters:
    artifactVerificationPolicies:
      "application/vnd.dev.cosign.artifact.sig.v1+json": "any"
      default: "any"
```

### Criar o constraint template

Por padrão, um [constraint template](https://open-policy-agent.github.io/gatekeeper/website/docs/constrainttemplates) do Gatekeeper usa a sintaxe Rego v0. Este exemplo habilita a sintaxe v1. Se quiser usar a sintaxe v0, será preciso atualizar a política. O exemplo também adiciona uma lista de imagens isentas, para permitir imagens específicas sem assinatura.

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredimagesignatures
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredImageSignatures
      validation:
        openAPIV3Schema:
          type: object
          properties:
            exemptImages:
              type: array
              items:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      code:
        - engine: Rego
          source:
            version: "v1"
            rego: |
              package k8srequiredimagesignatures

              default exemptions := []

              exemptions := input.parameters.exemptImages

              all_images contains val.image if {
                  containers := object.get(input.review.object.spec.template.spec, "containers", [])
                  initContainers := object.get(input.review.object.spec.template.spec, "initContainers", [])
                  ephContainers := object.get(input.review.object.spec.template.spec, "ephemeralContainers", [])

                  vals := array.concat(containers, array.concat(initContainers, ephContainers))
                  some val in vals
              }

              ratify_response(image) = resp if {
                      resp := external_data({
                        "provider": "ratify-provider",
                        "keys": [image],
                      })
              }

              responses contains {"image": resp[0], "data": resp[1]} if {
                some image in all_images
                not image in exemptions

                rat_resp := ratify_response(image)
                resp := rat_resp.responses[_]
              }

              violation contains {"msg": msg} if {
                some resp in responses
               resp.data.system_error != ""
               msg := sprintf("image %q verification system error: %v", [resp.image, resp.data.system_error])
              }

              violation contains {"msg": msg} if {
                some resp in responses
               count(resp.data.responses) == 0
               msg := sprintf("image %q returned no verification response", [resp.image])
              }

              violation contains {"msg": msg} if {
                some resp in responses
                not resp.data.isSuccess
               reason := object.get(resp.data, "message", "verification failed")
               msg := sprintf("image %q is not signed by Chainguard: %v", [resp.image, reason])
              }

              violation contains {"msg": msg} if {
                some resp in responses
               err := resp.data.errors[_]
                err[0] == resp.image
               msg := sprintf("image %q verification error: %v", [resp.image, err[1]])
              }
```

### Criar a constraint

A constraint vincula o constraint template aos tipos (kinds) do Kubernetes que você definir.

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredImageSignatures
metadata:
  name: require-signed-images
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
      - apiGroups: ["apps"]
        kinds: ["Deployment", "StatefulSet", "DaemonSet", "ReplicaSet"]
  parameters:
    exemptImages:
      - "registry.k8s.io/pause:3.9"

```

### Testar a implantação de uma imagem da Chainguard

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-chainguard
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-chainguard
  template:
    metadata:
      labels:
        app: nginx-chainguard
    spec:
      containers:
        - name: nginx
          image: cgr.dev/chainguard/nginx:latest
          ports:
            - containerPort: 8080
```

Isso deve criar a implantação com sucesso.

### Testar a implantação de uma imagem que não é da Chainguard

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-unsigned
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-unsigned
  template:
    metadata:
      labels:
        app: nginx-unsigned
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80

```

Você receberá um erro como este, explicando que a implantação foi bloqueada porque a imagem não foi assinada pela Chainguard.

```output
Error from server (Forbidden): error when creating "bad-deployment.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [require-signed-images] image "docker.io/library/nginx@sha256:7150b3a39203cb
5bee612ff4a9d18774f8c7caf6399d6e8985e97e28eb751c18" is not signed by Chainguard: verification failed
```

## Saiba mais

Ao combinar o OPA Gatekeeper com as imagens de contêiner da Chainguard, você ganha uma forma eficaz de aplicar segurança e conformidade em todos os seus clusters Kubernetes. O Gatekeeper garante que somente imagens de contêiner que atendem às políticas definidas sejam implantadas, enquanto os Chainguard Containers oferecem uma base mínima e protegida que reduz o risco desde o início. Juntos, eles ajudam as equipes a entregar software com mais segurança e confiança, sem desacelerar o desenvolvimento.

Para saber mais sobre o Gatekeeper, consulte a [documentação oficial](https://open-policy-agent.github.io/gatekeeper/website/docs/).
