---
title: "FIPS e algoritmos não aprovados"
linktitle: "FIPS e algoritmos não aprovados"
type: "article"
description: "Análise técnica de como as imagens FIPS da Chainguard dão acesso a algoritmos não aprovados, como MD5 e SHA1"
date: 2025-10-28T08:00:00+00:00
lastmod: 2026-10-01T00:00:00+00:00
draft: false
tags: ["FIPS", "MD5"]
images: []
weight: 60
toc: true
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

## Visão geral

Os módulos criptográficos FIPS implementam uma proteção criptograficamente forte dos dados em repouso e em trânsito. A posição do NIST sobre isso é muito clara ([fonte](https://csrc.nist.gov/projects/cryptographic-module-validation-program), tradução livre):

> A criptografia não validada é considerada como não oferecendo nenhuma proteção às informações ou aos dados; na prática, os dados seriam considerados texto simples desprotegido. Se o órgão especificar que as informações ou os dados devem ser protegidos criptograficamente, então o FIPS 140-2 ou o FIPS 140-3 se aplica. Em essência, se a criptografia for exigida, ela deve ser validada. Caso o módulo criptográfico seja revogado, o uso desse módulo deixa de ser permitido.

## Orientações do NIST sobre o uso de algoritmos não aprovados

Como parte do conjunto de publicações FIPS, o NIST publica o [FIPS 140-3 Implementation Guidance](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-ig-announcements) (FIPS 140 I.G.). Os requisitos do Cryptographic Module Validation Program (CMVP) para o FIPS 140-3 incluem normas ISO, documentos da série SP 800 e o FIPS 140-3 I.G. O conjunto completo de documentos e o diagrama estão disponíveis no [Computer Security Resource Center do NIST Information Technology Laboratory](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/fips-140-3-standards).

A seção 2.4.A do FIPS 140-3 I.G., "Definition and Use of a non-Approved Security Function", tem três páginas e deve ser lida em conjunto com todas as outras publicações relevantes do NIST e da ISO. Ela traz muitos exemplos, exceções e ressalvas que, em alguns casos, permitem usar algoritmos não aprovados como parte de serviços aprovados de nível mais alto. Por exemplo, alguns algoritmos podem não ser seguros quando usados diretamente, mas, com as salvaguardas adequadas, podem ser criptograficamente seguros. Isso costuma acontecer com protocolos complexos como o TLS, que combina primitivas criptográficas de forma segura.

Passando direto para os comentários adicionais, vamos nos concentrar nas declarações a seguir (edição atual; consulte o [FIPS 140-3 I.G.](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-ig-announcements) vigente para verificar eventuais mudanças).

### Comentário adicional da seção 2.4.A do FIPS 140-3 I.G.

Tradução livre:

O fornecedor deve apresentar documentação e justificativa claras de por que os algoritmos criptográficos não aprovados podem ser usados em um modo aprovado, ou seja, sem serem usados para atender aos requisitos das seções 6 e 7 do FIPS 140-3. Cabe ao CMVP determinar se esse uso de um algoritmo se enquadra nas orientações descritas nesta implementation guidance (IG).

Além disso, tentativas de usar esta IG para incluir algoritmos no modo aprovado não serão aceitas, a menos que todas as condições a seguir sejam atendidas:

1) o algoritmo não é usado de forma alguma para atender a qualquer requisito do FIPS 140-3;
1) o algoritmo não acessa nem compartilha CSPs de uma forma que contrarie os requisitos desta IG;
1) o algoritmo é:
   1) não destinado a ser usado como função de segurança (por exemplo, para interoperabilidade ou para nivelamento de desgaste de memória);
   1) redundante em relação a um algoritmo aprovado (como na criptografia dupla); ou
   1) uma operação criptográfica ou matemática aplicada "por garantia", mas não para oferecer segurança sólida (ou seja, aplicar XOR entre um CSP e um valor secreto, usar um algoritmo proprietário ou usar algoritmos não aprovados para ofuscar CSPs armazenados, que são considerados texto simples);
1) o uso e a finalidade não aprovados do algoritmo (do item 3, acima) são inequívocos para o operador e não podem ser facilmente confundidos com uma função de segurança.

### Compromisso da Chainguard com o FIPS

Conforme documentado no [compromisso da Chainguard com o FIPS](https://www.chainguard.dev/legal/fips-commitment), nossas imagens FIPS habilitam por padrão apenas serviços e algoritmos aprovados. Como usamos somente serviços aprovados, fica mais simples raciocinar, auditar e testar o que é ou não uma função de segurança. Por exemplo, a imagem [gradle-fips](https://images.chainguard.dev/directory/image/gradle-fips/versions) da Chainguard foi modificada para usar um keystore aprovado para armazenar as configurações de build. Embora isso não seja uma função de segurança, garantiu que nenhum keystore não aprovado pudesse vazar para o processo de build e para os testes.

Todos os casos de uso que possam estar relacionados a uma função de segurança também foram ajustados para usar apenas serviços aprovados. Isso inclui, entre outros:

* criptografia e descriptografia
* criação e verificação de assinaturas digitais
* geração de números aleatórios
* código de autenticação de mensagem
* funções de derivação de chave
* métodos de encapsulamento de chave
* troca de chaves

A única funcionalidade que tende a ser uma função que não é de segurança é o cálculo de um digest isolado, que não faz parte de um MAC, HMAC, árvore de Merkle, esquema de integridade ou assinatura digital. Especificamente, MD4, MD5 e SHA1 são universalmente obsoletos e proibidos em esquemas de segurança, mas continuam amplamente usados em funcionalidades que não são de segurança.

Exemplos desse uso que não é de segurança:

* O Webpack 4 usa MD4 para pré-calcular tabelas hash perfeitas a partir de entradas confiáveis no momento do build. Consulte [este issue](https://github.com/webpack/webpack/issues/14560).
* Yarn, .ZIP, JAR e PDF exigem MD5 como parte dos formatos de arquivo congelados que usam.
* O Amazon S3 aceita vários algoritmos para verificar a integridade de objetos por um canal confiável, incluindo MD5 e SHA1. Consulte [a documentação oficial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html). Muitas implementações de cliente usam MD5 por padrão.
* O Google Cloud Storage pode usar CRC32C ou MD5, e os clientes normalmente usam MD5 por padrão para verificar a integridade dos objetos durante os uploads ([documentação](https://docs.cloud.google.com/storage/docs/data-validation)).
* O AES-ECB é inseguro quando usado diretamente, mas é usado pelos protocolos QUIC e DTLSv1.3 para ofuscar informações públicas, sem fins de segurança.
* O SHA-1 ainda é amplamente usado para conteúdo endereçável por hash e tabelas de consulta, por exemplo no `apk-tools` e no git.

Em todos esses casos de uso, o cálculo do digest não oferece nenhuma funcionalidade de segurança: ele serve para detectar corrupção acidental ou melhorar o desempenho. Em geral, os dados são protegidos por SHA2-256 e transmitidos por um canal TLS seguro e autenticado.

Uma alternativa a migrar do MD5 é escolher uma função especializada, projetada explicitamente para fins que não são de segurança e com desempenho muito maior, como o [XXHASH](https://xxhash.com/). Na maioria dos casos, funcionalidades que não são de segurança devem migrar de CRC32C, MD5 e SHA1 para XXHASH3.

No entanto, se você precisa de interoperabilidade com formatos e serviços existentes *e* está estabelecido que o digest é usado para fins que não são de segurança, você precisa usar os digests inseguros. A Chainguard está integrando o suporte a esses casos de uso para MD5 e SHA1 em todas as suas imagens FIPS. Cada linguagem e cada aplicação têm uma implementação muito diferente e específica, documentada a seguir.

Embora o SHA1 seja aprovado atualmente, ele já é considerado obsoleto pelas RFCs. O NIST vai descontinuar o SHA1 até 2030. As implementações a seguir são voltadas para o futuro e buscam garantir o acesso ao MD5 hoje e ao SHA1 no futuro.

O SHA1 está disponível como aprovado nas versões 3.0.9, 3.1.2 e 3.4.0 do Chainguard FIPS Provider for OpenSSL. Ele passa a ser não aprovado a partir da versão 3.6.0.

## Acesso a algoritmos não aprovados para fins que não são de segurança

### Chainguard Legacy Approved provider for OpenSSL

As imagens FIPS e não FIPS da Chainguard são configuradas para usar um provider legado que expõe os algoritmos mencionados acima para fins que não são de segurança. Em tempo de execução, é possível desabilitá-los com a variável de ambiente `CHAINGUARD_LEGACY_APPROVED=0`. Esse provider permite que todas as aplicações OpenSSL acessem de maneira uniforme os algoritmos legados para fins que não são de segurança. Eles continuam bloqueados dentro dos limites do módulo FIPS para fins de segurança, como a proteção de dados em repouso ou em trânsito.

Esta orientação se aplica a todas as imagens e a todo software que usa OpenSSL:

* python-fips
* node-fips
* jdk-openssl-fips
* postgresql-fips
* dotnet-fips

Entre muitos outros.

### grpc, pyca e cryptography do Python com FIPS e MD5

Se você compila o grpc ou o pycryptography a partir do código-fonte, ou os instala pelo PyPI, eles podem incluir uma cópia vendorizada e vinculada estaticamente de uma biblioteca criptográfica e não vão operar no modo FIPS. Nesses casos, todo uso dessa biblioteca pode ser não aprovado.

Se você instalar o grpc e o pycryptography por meio do [Custom Assembly](https://edu.chainguard.dev/chainguard/containers/custom-assembly/overview/), eles serão vinculados dinamicamente ao OpenSSL da Chainguard e seguirão a orientação acima.

### Go-fips / Go-openssl-fips

O acesso ao digest MD5 é oferecido pela implementação nativa do Go, enquanto qualquer forma de autenticação, autorização, assinatura digital e TLS com MD5 é bloqueada.

### Todos os outros projetos

Se você tiver dúvidas sobre esta orientação ou sobre quaisquer outros pacotes, projetos, linguagens ou ecossistemas, selecione "Não" na seção de feedback desta página e preencha o formulário, ou [abra um chamado de suporte](https://support.chainguard.dev/).
