---
title: "¿Qué es Chainguard?"
linktitle: "¿Qué es Chainguard?"
lead: "Una introducción general a Chainguard: el problema que resuelve, los productos que ofrece y lo que los hace diferentes."
description: "Una visión general de Chainguard: su misión de ser la fuente segura del código abierto, sus productos (Containers, Libraries y OS) y la Factory que los compila."
type: "article"
date: 2026-07-23T00:00:00+00:00
lastmod: 2026-10-14T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 10
translation:
  sourceLastmod: 2026-10-13T13:59:25+00:00
  reviewed: false
---

Casi todas las aplicaciones modernas se basan en software de código abierto. Ese software es potente, pero llega con problemas: vulnerabilidades (incluidos los CVE divulgados públicamente), dependencias sin parches, procedencia poco clara y el trabajo constante de mantenerlo todo actualizado. Rastrear y corregir estos problemas en una base de código grande consume tiempo de ingeniería que podría dedicarse a crear productos.

La misión de Chainguard es ser la fuente segura del código abierto. En lugar de dejar que usted aplique parches y refuerce el software de código abierto por su cuenta, Chainguard lo recompila a partir del código fuente en un entorno de build reforzado, lo mantiene actualizado de forma continua y lo distribuye con los metadatos que necesita para verificar lo que ejecuta. El resultado es software con pocos o ningún CVE conocido y que exige mucho menos trabajo de corrección a su equipo.

## Qué ofrece Chainguard

Chainguard recompila software de código abierto en productos que puede adoptar directamente, según cómo consuma sus dependencias:

- **[Chainguard Containers](/chainguard/containers/overview/)** es una colección de imágenes de contenedor mínimas y reforzadas. Siguiendo una filosofía distroless, cada imagen incluye solo su aplicación y sus dependencias de ejecución esenciales, lo que reduce al mínimo la superficie de ataque. Este minimalismo es en gran parte la razón por la que tienen [pocos o ningún CVE](/chainguard/containers/concepts/zerocve/).
- **[Chainguard Libraries](/chainguard/libraries/introduction/overview/)** aplican el mismo enfoque a las dependencias de lenguaje. Son reemplazos directos de paquetes de código abierto en los ecosistemas de Java, Python y JavaScript, recompilados a partir de fuentes verificadas y supervisados de forma continua.

Las Chainguard Containers y Libraries se descargan desde un único endpoint que aplica políticas: el [Chainguard Repository](/chainguard/chainguard-repository/overview/).

La mayoría de los equipos comienza con Containers y Libraries, pero Chainguard protege mucho más. Sus otros productos incluyen:

- **[Chainguard OS](/chainguard/chainguard-os/overview/)**, la base Linux reforzada sobre la que se construyen los demás productos.
- **[Chainguard VMs](/chainguard/vms/overview/)**, imágenes mínimas de máquinas virtuales para cargas de trabajo en la nube y en hipervisores.
- **[Chainguard Actions](/chainguard/actions/overview/)**, reemplazos reforzados de GitHub Actions populares.
- **[Guardener](/chainguard/guardener/)**, herramientas para reforzar su propio código fuente.
- **[Chainguard Agent Skills](/chainguard/agent-skills/overview/)**, skills revisadas en cuanto a seguridad para agentes de IA.
- **[Chainguard Checks](/chainguard/checks/overview/)**, CI para pull requests de GitHub que ejecuta cada comprobación en su propia microVM aislada.
- **[Chainguard Workspaces](/chainguard/workspaces/overview/)**, sesiones remotas en microVM para desarrollo y agentes de programación que mantienen sus credenciales fuera de la sesión.

## La Chainguard Factory

Detrás de estos productos está la [Chainguard Factory](/platform/factory/overview/), el sistema de build automatizado que es el núcleo de lo que hace Chainguard. La Factory supervisa de forma continua miles de proyectos de código abierto. Cuando aparece una nueva versión upstream, obtiene el código fuente, lo verifica, lo recompila, lo vuelve a probar y publica paquetes firmados compilados a partir del código fuente, junto con SBOM y metadatos de procedencia.

Como la Factory hace este trabajo por usted, adoptar un artefacto de Chainguard reduce de inmediato el riesgo de su cadena de suministro de software. Como Chainguard mantiene el artefacto de forma continua, esas mejoras de seguridad se mantienen con el tiempo con cambios mínimos en sus flujos de trabajo actuales.

## Por qué Chainguard

En comparación con los artefactos de repositorios públicos, Chainguard le ofrece:

- **Pocos o ningún CVE**, para que su equipo dedique menos tiempo a clasificar vulnerabilidades y aplicar parches.
- **Una superficie de ataque mínima**, porque los artefactos incluyen solo lo que necesitan para ejecutarse.
- **Procedencia verificable** mediante firmas, SBOM y builds a partir del código fuente, para que pueda demostrar qué hay en su cadena de suministro de software.
- **Actualizaciones continuas**, para que los parches lleguen automáticamente en lugar de esperar actualizaciones manuales.

## Próximos pasos

- ¿Listo para probar una imagen? Siga un [ejemplo de contenedor](/get-started/containers-examples/) para su lenguaje o servicio.
- ¿Prefiere reemplazar dependencias? Comience con la [introducción a las bibliotecas](/get-started/libraries-examples/).
- ¿Va a trasladar cargas de trabajo existentes? Siga las [guías de migración](/get-started/migration/).
- ¿Va a implementar Chainguard en sus equipos? Descubra cómo [incorporar a sus equipos](/get-started/onboard-your-teams/).
