---
title: "Obtener soporte"
linktitle: "Obtener soporte"
lead: "Chainguard ofrece varias formas de obtener ayuda, y la adecuada depende de su situación. Esta guía explica qué revisar primero, qué canal atiende su tipo de solicitud y cómo abrir un ticket de soporte cuando lo necesite."
description: "Obtenga ayuda de Chainguard: revise las opciones de autoservicio, elija el canal de soporte adecuado y abra un ticket con el que un ingeniero de soporte pueda trabajar."
type: "article"
date: 2026-09-01T00:00:00+00:00
lastmod: 2026-10-14T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 50
toc: true
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

Cuando la documentación no responde a su pregunta, Chainguard ofrece varias formas de obtener ayuda. Esta guía explica qué revisar primero, qué canal atiende su tipo de solicitud y cómo abrir un ticket de soporte cuando lo necesite.

## Antes de abrir un ticket

Muchas preguntas ya tienen una respuesta publicada que puede encontrar en segundos:

- **Este sitio de documentación.** Busque desde el cuadro de la parte superior de cualquier página.

- **Preguntar a la IA.** Haga clic en **Preguntar a la IA** en la esquina superior derecha de cualquier página de este sitio y formule su pregunta en lenguaje natural. El asistente se basa en la documentación y el contenido de soporte de Chainguard, y cita sus fuentes. Revise la respuesta y sus fuentes antes de actuar en consecuencia.

- **La [base de conocimientos de Chainguard](https://support.chainguard.dev/hc/en-us).** Los ingenieros de soporte de Chainguard publican allí artículos sobre problemas que se repiten.

## Adónde enviar su solicitud

El portal de soporte atiende la mayoría de las solicitudes, pero no es la única vía y, en algunas situaciones, no es la adecuada. Busque su situación en la siguiente lista:

- **Tiene un problema con un producto de Chainguard o con la configuración de su organización.** Abra un ticket en el [portal de soporte](https://support.chainguard.dev/).

- **Necesita trasladar su autenticación multifactor a un nuevo dispositivo, o perdió el dispositivo que ejecuta su aplicación de autenticación.** Dónde se hace ese cambio depende de cómo inicia sesión y, en la mayoría de los casos, no es Chainguard quien gestiona su MFA. Consulte [Cambiar o restablecer su dispositivo de MFA](/get-started/mfa-devices/).

- **No puede iniciar sesión de ningún modo, así que no puede acceder al portal.** Envíe un correo electrónico a [support@chainguard.dev](mailto:support@chainguard.dev).

- **Su organización usa Catalog Starter.** Use la [base de conocimientos](https://support.chainguard.dev/hc/en-us), el [Slack de la comunidad](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw) y los [cursos de Chainguard](https://courses.chainguard.dev/) gratuitos. Catalog Starter no incluye acceso a tickets.

- **Su solicitud se refiere a su suscripción o a lo que su organización tiene licenciado; por ejemplo, si una imagen determinada está incluida en sus derechos de uso.** Comuníquese con su equipo de cuenta, es decir, el gerente de éxito del cliente o el arquitecto de soluciones asignado a su organización.

- **No puede descargar una imagen de contenedor o una versión específica de una.** Siga primero [Solucionar problemas de disponibilidad de contenedores y versiones](/chainguard/containers/troubleshooting/container-version-troubleshooting/). Allí se indica qué casos puede resolver usted mismo y cuáles requieren un ticket.

## Abrir un ticket

### Confirmar que puede acceder al portal

El portal de soporte tiene dos requisitos previos.

En primer lugar, su organización necesita un plan de pago. Catalog Starter no incluye tickets de soporte ni análisis de causa raíz. Para saber qué cubre el plan gratuito, consulte [Chainguard Catalog Starter](/chainguard/containers/reference/catalog-starter/).

En segundo lugar, su identidad debe estar vinculada a una organización. El portal lo identifica a través de su cuenta de Chainguard Console, y una identidad no vinculada produce un error. Para comprobarlo, inicie sesión en [Chainguard Console](https://console.chainguard.dev) y busque su organización en la barra lateral izquierda. Si no aparece, pida a un administrador de su organización que lo invite y, luego, abra el correo electrónico de invitación y complete el flujo de configuración. Si inicia sesión sin completar ese flujo, su identidad queda sin vincular.

{{< note >}}
Los administradores pueden invitar usuarios desde la Console, en **Settings > Users > Invite users**, o desde la línea de comandos. Consulte [Cómo gestionar organizaciones de IAM en Chainguard](/platform/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/).
{{< /note >}}

### Enviar la solicitud

1. Inicie sesión en [Chainguard Console](https://console.chainguard.dev).

1. En la barra lateral izquierda, haga clic en **Support**. También puede ir directamente a [support.chainguard.dev](https://support.chainguard.dev/).

1. Complete el formulario de solicitud. Antes de enviarlo, el portal le ofrece documentación relevante y una respuesta generada. Si eso resuelve su pregunta, ha terminado. De lo contrario, envíe la solicitud de la forma habitual.

### Si el portal devuelve un error

Siga estos pasos:

1. Abra la Console y el portal de soporte en una ventana de navegación privada.

1. Borre la caché y las cookies del navegador.

1. Confirme que inicia sesión con la misma identidad con la que lo invitaron.

Si el error persiste, envíe un correo electrónico a [support@chainguard.dev](mailto:support@chainguard.dev) con una captura de pantalla del error, la dirección de correo electrónico de la cuenta que intenta usar y el enlace de invitación, si todavía lo tiene.

## Qué incluir en su solicitud

Un ingeniero de soporte puede empezar a trabajar en un problema, en lugar de pedirle más información, cuando su solicitud incluye:

- El nombre de su organización.

- El nombre y la etiqueta de la imagen o del paquete y, si lo tiene, el digest.

- El comando que ejecutó y su salida completa, incluido cualquier mensaje de error.

- La versión de `chainctl`, si el problema involucra la herramienta de línea de comandos. Ejecute `chainctl version` para obtenerla.

- Lo que esperaba que ocurriera.

- Cualquier otra cosa que crea que puede ayudar: logs, capturas de pantalla o una breve grabación de pantalla.
