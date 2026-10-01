---
title: "O que é a Chainguard?"
linktitle: "O que é a Chainguard?"
lead: "Uma introdução geral à Chainguard: o problema que ela resolve, os produtos que oferece e o que os torna diferentes."
description: "Uma visão geral da Chainguard: sua missão de ser a fonte segura de código aberto, seus produtos (Containers, Libraries e OS) e a Factory que os cria."
type: "article"
date: 2026-07-23T00:00:00+00:00
lastmod: 2026-10-01T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 10
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

Quase todos os aplicativos modernos são criados com software de código aberto. Esse software é poderoso, mas traz problemas: vulnerabilidades (incluindo CVEs divulgadas publicamente), dependências sem correção, procedência pouco clara e o trabalho constante de manter tudo atualizado. Rastrear e corrigir esses problemas em uma base de código grande consome um tempo de engenharia que poderia ser dedicado à criação de produtos.

A missão da Chainguard é ser a fonte segura de código aberto. Em vez de deixar que você mesmo corrija e proteja o software de código aberto, a Chainguard o recompila a partir do código-fonte em um ambiente de build protegido, o mantém atualizado continuamente e o distribui com os metadados de que você precisa para verificar o que está executando. O resultado é um software com poucas ou nenhuma CVE conhecida e que exige muito menos trabalho de correção da sua equipe.

## O que a Chainguard oferece

A Chainguard recompila software de código aberto em produtos que você pode adotar diretamente, de acordo com a forma como você consome dependências:

- **[Chainguard Containers](/chainguard/containers/overview/)** são imagens de contêiner mínimas e protegidas. Seguindo a filosofia distroless, cada imagem inclui apenas o seu aplicativo e as dependências de tempo de execução essenciais, o que reduz a superfície de ataque. Esse minimalismo é um dos principais motivos pelos quais elas têm [poucas ou nenhuma CVE](/chainguard/containers/concepts/zerocve/).
- **[Chainguard Libraries](/chainguard/libraries/introduction/overview/)** aplicam a mesma abordagem às dependências de linguagem. Elas substituem diretamente pacotes de código aberto dos ecossistemas Java, Python e JavaScript, são recompiladas a partir de fontes verificadas e monitoradas continuamente.

Você baixa os Chainguard Containers e as Chainguard Libraries de um único endpoint que aplica políticas, o [Chainguard Repository](/chainguard/chainguard-repository/overview/).

A maioria das equipes começa pelos Containers e pelas Libraries, mas a Chainguard protege mais do que isso. Os outros produtos incluem:

- **[Chainguard OS](/chainguard/chainguard-os/overview/)**, a base Linux protegida sobre a qual os outros produtos são criados.
- **[Chainguard VMs](/chainguard/vms/overview/)**, imagens mínimas de máquina virtual para cargas de trabalho em nuvem e em hipervisores.
- **[Chainguard Actions](/chainguard/actions/overview/)**, substitutos protegidos para GitHub Actions populares.
- **[Guardener](/chainguard/guardener/)**, ferramentas para proteger o seu próprio código-fonte.
- **[Chainguard Agent Skills](/chainguard/agent-skills/overview/)**, skills para agentes de IA com revisão de segurança.

## A Chainguard Factory

Por trás desses produtos está a [Chainguard Factory](/platform/factory/overview/), o sistema de build automatizado que é o centro do trabalho da Chainguard. A Factory monitora continuamente milhares de projetos de código aberto. Quando surge uma nova versão upstream, ela obtém o código-fonte, verifica, recompila, testa novamente e publica pacotes assinados, criados a partir do código-fonte, junto com SBOMs e metadados de procedência.

Como a Factory faz esse trabalho por você, adotar um artefato da Chainguard reduz imediatamente o risco da sua cadeia de suprimentos de software. Como a Chainguard mantém o artefato continuamente, essas melhorias de segurança continuam ao longo do tempo, com mudanças mínimas nos seus fluxos de trabalho.

## Por que a Chainguard

Em comparação com artefatos de repositórios públicos, a Chainguard oferece:

- **Poucas ou nenhuma CVE**, para que sua equipe gaste menos tempo triando e corrigindo vulnerabilidades.
- **Uma superfície de ataque mínima**, porque os artefatos incluem apenas o que precisam para funcionar.
- **Procedência verificável** por meio de assinaturas, SBOMs e builds a partir do código-fonte, para que você possa comprovar o que há na sua cadeia de suprimentos de software.
- **Atualizações contínuas**, para que as correções cheguem automaticamente em vez de esperar por atualizações manuais.

## Próximos passos

- Pronto para testar uma imagem? Siga um [exemplo de contêiner](/get-started/containers-examples/) para sua linguagem ou serviço.
- Vai substituir dependências? Comece pela [introdução às bibliotecas](/get-started/libraries-examples/).
- Vai migrar cargas de trabalho existentes? Siga os [guias de migração](/get-started/migration/).
- Vai levar a Chainguard para suas equipes? Veja como [integrar suas equipes](/get-started/onboard-your-teams/).
