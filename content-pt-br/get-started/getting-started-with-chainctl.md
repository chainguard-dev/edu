---
title: "Primeiros passos com o chainctl"
lead: "A CLI chainctl da Chainguard permite gerenciar com mais segurança imagens de contêiner e recursos de IAM pela linha de comando, em fluxos de trabalho de DevOps e segurança."
description: "Primeiros passos com o chainctl: autenticação, gerenciamento de organizações e comandos essenciais da plataforma de segurança de contêineres da Chainguard"
type: "article"
date: 2025-03-03T08:49:15+00:00
lastmod: 2026-10-01T00:00:00+00:00
draft: false
tags: ["chainctl", "Getting Started"]
images: []
weight: 80
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

O `chainctl` da Chainguard oferece acesso pela linha de comando para gerenciar imagens de contêiner, recursos de identidade e configurações de segurança em toda a sua organização. Este guia apresenta os comandos essenciais para começar a usar o `chainctl` nos seus fluxos de trabalho de segurança e DevOps. Para a documentação completa dos comandos, consulte a [referência do chainctl](/platform/chainctl/).

## Autenticar e verificar o status da autenticação

Para usar o `chainctl`, a primeira coisa a fazer é [se autenticar na plataforma da Chainguard](/chainguard/containers/registry/authenticating/). Para isso, execute:

```shell
chainctl auth login
```

Será exibida uma lista de provedores de identidade para você escolher. Use o que está vinculado à sua conta da Chainguard. Depois que você escolher o provedor, como o Google, o `chainctl` abrirá uma janela do navegador para você fazer login com suas credenciais. Após o login, você poderá salvar esse provedor de identidade como padrão para os próximos logins. Em seguida, um token será trocado e você poderá usar o `chainctl`.

{{< blurb/chainctl-auth >}}

Para verificar o status da autenticação a qualquer momento, execute:

```shell
chainctl auth status
```

Esse comando mostra sua identidade e outros atributos vinculados à sua conta, incluindo os papéis e as capacidades atribuídos a ela.

Para criar um token de pull, use:

```shell
chainctl auth pull-token
```

Uma flag importante desse comando é `--repository`, que permite especificar o tipo de repositório para o qual o token de pull será criado. Por exemplo, `--repository=apk` vincula a identidade do token de pull ao papel `apk.pull`, o que permite que a identidade baixe pacotes do repositório APK privado da organização pai.

Para configurar um auxiliar de credenciais do Docker, que usará um token para baixar imagens quando você usar o Docker, execute:

```shell
chainctl auth configure-docker
```

> **Observação**: {{< blurb/noproxy >}}

## Atualizar o chainctl para a versão mais recente

Para ver qual versão do `chainctl` está instalada, use:

```shell
chainctl version
```

Para atualizar sua instalação do `chainctl`, use:

```shell
chainctl update
```

Como esse comando substitui o binário instalado, você precisa de permissão de gravação no diretório em que o `chainctl` está. No Linux e no macOS, atualizar uma instalação para todo o sistema, como em `/usr/local/bin`, exige privilégios de administrador (por exemplo, com `sudo`). O comando também verifica a assinatura do binário baixado antes de instalá-lo. Para mais detalhes, consulte [Atualizar o chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

## Configurar o chainctl

O `chainctl` vem com uma configuração padrão, mas alguns aspectos dela podem ser ajustados. Um exemplo é definir o local do registro usado quando um comando não especifica um. Para editar a configuração atual, use:

```shell
chainctl config edit
```

Se você cometer um erro e não lembrar das configurações originais, restaure a configuração padrão com:

```shell
chainctl config reset
```

Saiba mais em [Como gerenciar a configuração do chainctl](/platform/chainctl-usage/manage-chainctl-config/).

## Listar as imagens disponíveis

Para ver quais Chainguard Containers estão disponíveis para sua conta, use:

```shell
chainctl images list
```

Atenção: essa lista pode demorar para ser gerada e provavelmente vai rolar rapidamente no seu terminal.

## Comparar duas versões de uma imagem

Digamos que você queira comparar duas versões de uma imagem do mesmo pacote. Você precisa saber a URL do seu repositório, o nome da imagem e as duas versões que quer comparar. Para as versões, você pode usar números de release, como `8.12.0`, ou `latest` e `latest-dev`.

Use o comando a seguir, que mostra o repositório usado pela equipe de Developer Education da Chainguard. As duas ocorrências de `<image_name>` são iguais:

```shell
chainctl images diff cgr.dev/chainguard.edu/$IMAGENAME:latest cgr.dev/chainguard.edu/$IMAGENAME:latest-dev
```

Se a imagem ou a release solicitada não estiver disponível no repositório que você está usando, o comando retornará um erro `Forbidden`, da mesma forma que ao tentar baixar uma imagem a que você não tem acesso ou de um repositório que sua conta não tem autorização para usar.

Saiba mais em [Como comparar Chainguard Containers com o chainctl](/platform/chainctl-usage/comparing-images/).

## Listar as versões de pacotes disponíveis

Para ver detalhes sobre as versões de pacotes disponíveis para uso em imagens, use:

```shell
chainctl packages versions list $PACKAGENAME
```

Esse comando lista todas as versões que a Chainguard compilou e a data de fim de vida útil de cada versão que tiver uma. Ele também lista versões mais antigas de pacotes que não estão mais disponíveis.

## Formatos de saída

Os comandos podem ter um formato de saída padrão, mas você não precisa se limitar a ele. Há uma opção para informar ao `chainctl` qual formato de saída usar:

```shell
chainctl $COMMAND -o $FORMAT
```

O `-o` deve ser seguido por uma destas strings: `csv`, `id`, `json`, `none`, `table`, `terse`, `tree` ou `wide`.

Nem todos os formatos de saída fazem sentido para todos os comandos, então teste bem antes de usar um formato específico em automações.
