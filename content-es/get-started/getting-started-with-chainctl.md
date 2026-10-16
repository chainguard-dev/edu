---
title: "Primeros pasos con chainctl"
lead: "La CLI chainctl de Chainguard permite gestionar de forma más segura imágenes de contenedor y recursos de IAM desde la línea de comandos, en flujos de trabajo de DevOps y seguridad."
description: "Primeros pasos con chainctl: autenticación, gestión de organizaciones y comandos esenciales de la plataforma de seguridad de contenedores de Chainguard"
type: "article"
date: 2025-03-03T08:49:15+00:00
lastmod: 2026-10-14T00:00:00+00:00
draft: false
tags: ["chainctl", "Getting Started"]
images: []
weight: 80
translation:
  sourceLastmod: 2026-10-08T13:25:53+00:00
  reviewed: false
---

`chainctl` de Chainguard ofrece acceso desde la línea de comandos para gestionar imágenes de contenedor, recursos de identidad y configuraciones de seguridad en toda su organización. Esta guía presenta los comandos esenciales para empezar a usar `chainctl` de forma eficaz en sus flujos de trabajo de seguridad y DevOps. Para ver la documentación completa de los comandos, consulte la [referencia de chainctl](/platform/chainctl/).

## Autenticarse y comprobar el estado de la autenticación

Para usar `chainctl`, lo primero que debe hacer es [autenticarse en la plataforma de Chainguard](/chainguard/containers/registry/authenticating/). Para ello, ejecute:

```shell
chainctl auth login
```

Se muestra una lista de proveedores de identidad para que elija uno. Use el que esté vinculado a su cuenta de Chainguard. Cuando seleccione el que quiere usar, por ejemplo Google, `chainctl` abre una ventana del navegador para que inicie sesión con sus credenciales. Si el inicio de sesión se realiza correctamente, tiene la opción de guardar ese proveedor de identidad como predeterminado para los próximos inicios de sesión. Después se intercambia un token y ya puede usar `chainctl`.

{{< blurb/chainctl-auth >}}

Para comprobar el estado de su autenticación en cualquier momento, ejecute:

```shell
chainctl auth status
```

Este comando muestra su identidad y otros atributos vinculados a su cuenta, incluidos los roles y las capacidades asignados a ella.

Para crear un token de pull, use:

```shell
chainctl auth pull-token
```

Un flag importante que puede pasar a este comando es `--repository`, que permite especificar el tipo de repositorio para el que se crea el token de pull. Por ejemplo, si especifica `--repository=apk`, la identidad del token de pull se vincula al rol `apk.pull`, lo que le permite descargar paquetes del repositorio APK privado de la organización principal.

Para configurar un asistente de credenciales de Docker, que usa un token para descargar imágenes cuando usa Docker, use:

```shell
chainctl auth configure-docker
```

> **Nota**: {{< blurb/noproxy >}}

## Actualizar chainctl a la versión más reciente

Para ver qué versión de `chainctl` tiene instalada, use:

```shell
chainctl version
```

Para actualizar su instalación de `chainctl`, use:

```shell
chainctl update
```

Como este comando reemplaza el binario instalado, necesita permiso de escritura en el directorio donde se encuentra `chainctl`. En Linux y macOS, actualizar una instalación para todo el sistema, como `/usr/local/bin`, requiere privilegios de administrador (por ejemplo, con `sudo`). El comando también verifica la firma del binario descargado dentro del propio proceso antes de instalarlo; consulte [Actualizar chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl) para obtener más detalles.

## Configurar chainctl

`chainctl` incluye una configuración predeterminada, pero algunos de sus aspectos se pueden ajustar. Por ejemplo, puede definir la ubicación del registro que se usa cuando un comando no indica ninguna. Para editar la configuración actual, use:

```shell
chainctl config edit
```

Si comete un error y no recuerda la configuración original, restablezca la configuración predeterminada con:

```shell
chainctl config reset
```

Obtenga más información en [Cómo gestionar la configuración de chainctl](/platform/chainctl-usage/manage-chainctl-config/).

## Listar las imágenes disponibles

Para ver qué imágenes de contenedor están disponibles para su cuenta, use:

```shell
chainctl images list
```

Tenga en cuenta que generar esa lista puede tardar un poco y que es probable que se desplace rápidamente en su terminal de línea de comandos.

## Comparar dos versiones de una imagen

Supongamos que quiere comparar dos versiones de una imagen del mismo paquete. Necesita conocer la URL de su repositorio, el nombre de la imagen y las dos versiones que quiere comparar. Como versiones, puede usar números de versión como `8.12.0`, o bien `latest` o `latest-dev`.

Use el siguiente comando, donde mostramos el repositorio que usa nuestro equipo de Chainguard Developer Education y donde ambas instancias de `<image_name>` son iguales:

```shell
chainctl images diff cgr.dev/chainguard.edu/$IMAGENAME:latest cgr.dev/chainguard.edu/$IMAGENAME:latest-dev
```

Si la imagen o la versión solicitada no está disponible en el repositorio que usa, el comando devuelve un error `Forbidden`, igual que si intentara descargar una imagen a la que no tiene acceso o desde un repositorio que su cuenta no está autorizada a usar.

Obtenga más información en [Cómo comparar Chainguard Containers con chainctl](/platform/chainctl-usage/comparing-images/).

## Listar las versiones de paquetes disponibles

Si quiere obtener detalles sobre las distintas versiones de paquetes disponibles que se pueden usar en las imágenes, use:

```shell
chainctl packages versions list $PACKAGENAME
```

Este comando muestra todas las versiones que Chainguard ha compilado y la fecha de fin de vida de cada versión que tenga una asignada. También muestra las versiones de paquetes más antiguas que ya no están disponibles.

## Formatos de salida

Los comandos pueden tener un formato de salida predeterminado, pero eso no significa que tenga que mantenerlo. Existe una opción para indicarle a `chainctl` qué formato de salida usar, de la siguiente manera:

```shell
chainctl $COMMAND -o $FORMAT
```

Después de `-o` se indica una de las siguientes cadenas: `csv`, `id`, `json`, `none`, `table`, `terse`, `tree` o `wide`.

No todos los formatos de salida tienen sentido para todos los comandos, así que pruébelos bien antes de usar un formato específico en la automatización.
