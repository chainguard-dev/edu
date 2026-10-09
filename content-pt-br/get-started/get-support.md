---
title: "Obter suporte"
linktitle: "Obter suporte"
lead: "A Chainguard oferece várias formas de obter ajuda, e a mais adequada depende da sua situação. Este guia explica o que verificar primeiro, qual canal atende o seu tipo de solicitação e como abrir um chamado de suporte quando necessário."
description: "Obtenha ajuda da Chainguard: confira as opções de autoatendimento, escolha o canal de suporte certo e abra um chamado com as informações de que um engenheiro de suporte precisa."
type: "article"
date: 2026-09-01T00:00:00+00:00
lastmod: 2026-10-01T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 50
toc: true
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

Quando a documentação não responde à sua pergunta, a Chainguard oferece várias formas de obter ajuda. Este guia explica o que verificar primeiro, qual canal atende o seu tipo de solicitação e como abrir um chamado de suporte quando necessário.

## Antes de abrir um chamado

Muitas perguntas já têm uma resposta publicada que você encontra em segundos:

- **Este site de documentação.** Pesquise usando a caixa no topo de qualquer página.

- **Pergunte à IA.** Clique em **Pergunte à IA** no canto superior direito de qualquer página deste site e faça sua pergunta em linguagem natural. O assistente usa a documentação e o conteúdo de suporte da Chainguard e cita as fontes. Revise a resposta e as fontes antes de agir com base nela.

- **A [base de conhecimento da Chainguard](https://support.chainguard.dev/hc/en-us).** Os engenheiros de suporte da Chainguard publicam artigos sobre problemas recorrentes.

## Para onde enviar sua solicitação

O portal de suporte atende a maioria das solicitações, mas não é o único caminho e, em algumas situações, não é o mais adequado. Encontre a sua situação na lista a seguir:

- **Você tem um problema com um produto da Chainguard ou com a configuração da sua organização.** Abra um chamado no [portal de suporte](https://support.chainguard.dev/).

- **Você precisa mover sua autenticação multifator para um novo dispositivo ou perdeu o dispositivo com seu aplicativo autenticador.** O lugar onde você faz essa alteração depende de como você faz login e, na maioria dos casos, não é a Chainguard que gerencia sua MFA. Consulte [Alterar ou redefinir seu dispositivo de MFA](/get-started/mfa-devices/).

- **Você não consegue fazer login e, por isso, não consegue acessar o portal.** Envie um e-mail para [support@chainguard.dev](mailto:support@chainguard.dev).

- **Sua organização usa o Catalog Starter.** Use a [base de conhecimento](https://support.chainguard.dev/hc/en-us), o [Slack da comunidade](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw) e os [cursos gratuitos da Chainguard](https://courses.chainguard.dev/). O Catalog Starter não inclui acesso a chamados.

- **Sua solicitação é sobre a sua assinatura ou sobre o que sua organização tem licenciado, por exemplo, se uma determinada imagem está incluída nos seus direitos de uso.** Entre em contato com a equipe da sua conta, ou seja, o gerente de sucesso do cliente ou o arquiteto de soluções designado para a sua organização.

- **Você não consegue baixar uma imagem de contêiner ou uma versão específica dela.** Siga primeiro o guia [Solucionar problemas de disponibilidade de contêineres e versões](/chainguard/containers/troubleshooting/container-version-troubleshooting/). Ele indica quais casos você mesmo pode resolver e quais exigem um chamado.

## Abrir um chamado

### Confirme que você tem acesso ao portal

O portal de suporte tem dois pré-requisitos.

Primeiro, sua organização precisa ter um plano pago. O Catalog Starter não inclui chamados de suporte nem análise de causa raiz. Para saber o que o plano gratuito inclui, consulte [Chainguard Catalog Starter](/chainguard/containers/reference/catalog-starter/).

Segundo, sua identidade precisa estar vinculada a uma organização. O portal identifica você pela sua conta do Chainguard Console, e uma identidade sem vínculo gera um erro. Para verificar, faça login no [Chainguard Console](https://console.chainguard.dev) e procure sua organização na barra lateral esquerda. Se ela não aparecer, peça a um administrador da sua organização que envie um convite para você. Depois, abra o e-mail de convite e conclua o fluxo de configuração. Se você fizer login sem concluir esse fluxo, sua identidade continuará sem vínculo.

{{< note >}}
Os administradores podem convidar usuários pelo Console, em **Settings > Users > Invite users**, ou pela linha de comando. Consulte [Como gerenciar organizações IAM na Chainguard](/platform/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/).
{{< /note >}}

### Envie a solicitação

1. Faça login no [Chainguard Console](https://console.chainguard.dev).

1. Na barra lateral esquerda, clique em **Support**. Você também pode acessar [support.chainguard.dev](https://support.chainguard.dev/) diretamente.

1. Preencha o formulário de solicitação. Antes do envio, o portal sugere documentação relevante e uma resposta gerada automaticamente. Se isso resolver sua dúvida, não é preciso fazer mais nada. Caso contrário, envie a solicitação normalmente.

### Se o portal retornar um erro

Siga estas etapas:

1. Abra o Console e o portal de suporte em uma janela de navegação anônima.

1. Limpe o cache e os cookies do navegador.

1. Confirme que você está fazendo login com a mesma identidade que recebeu o convite.

Se o erro continuar, envie um e-mail para [support@chainguard.dev](mailto:support@chainguard.dev) com uma captura de tela do erro, o endereço de e-mail da conta que você está tentando usar e o link do convite, se ainda o tiver.

## O que incluir na sua solicitação

Um engenheiro de suporte consegue começar a trabalhar no problema, em vez de pedir mais informações, quando sua solicitação inclui:

- O nome da sua organização.

- O nome e a tag da imagem ou do pacote e, se tiver, o digest.

- O comando que você executou e a saída completa, incluindo qualquer mensagem de erro.

- A versão do `chainctl`, se o problema envolver a ferramenta de linha de comando. Execute `chainctl version` para obtê-la.

- O que você esperava que acontecesse.

- Qualquer outra informação que possa ajudar: logs, capturas de tela ou uma gravação de tela curta.
