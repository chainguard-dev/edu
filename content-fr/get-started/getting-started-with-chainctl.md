---
title: "Premiers pas avec chainctl"
lead: "La CLI chainctl de Chainguard permet de gérer de façon plus sécurisée les images de conteneur et les ressources IAM en ligne de commande, dans vos workflows DevOps et de sécurité."
description: "Premiers pas avec chainctl : authentification, gestion des organisations et commandes essentielles de la plateforme de sécurité des conteneurs de Chainguard"
type: "article"
date: 2025-03-03T08:49:15+00:00
lastmod: 2026-10-14T00:00:00+00:00
draft: false
tags: ["chainctl", "Getting Started"]
images: []
weight: 80
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

L'outil `chainctl` de Chainguard permet de gérer en ligne de commande les images de conteneur, les ressources d'identité et les configurations de sécurité de toute votre organisation. Ce guide présente les commandes essentielles pour bien démarrer avec `chainctl` dans vos workflows de sécurité et DevOps. Pour la documentation complète des commandes, consultez la [référence de chainctl](/platform/chainctl/).

## S'authentifier et vérifier l'état de l'authentification

Pour utiliser `chainctl`, vous devez d'abord [vous authentifier auprès de la plateforme Chainguard](/chainguard/containers/registry/authenticating/). Pour cela, exécutez :

```shell
chainctl auth login
```

La commande affiche une liste de fournisseurs d'identité parmi lesquels choisir. Choisissez celui qui est associé à votre compte Chainguard. Une fois votre choix fait, par exemple Google, `chainctl` ouvre une fenêtre de navigateur pour que vous vous connectiez avec vos identifiants. Une fois la connexion réussie, vous pouvez enregistrer ce fournisseur d'identité comme fournisseur par défaut pour vos prochaines connexions. Un jeton est ensuite échangé et vous pouvez utiliser `chainctl`.

{{< blurb/chainctl-auth >}}

Pour vérifier à tout moment l'état de votre authentification, exécutez :

```shell
chainctl auth status
```

La commande affiche votre identité et d'autres attributs associés à votre compte, notamment les rôles et les capacités attribués à votre compte.

Pour créer un jeton de pull, exécutez :

```shell
chainctl auth pull-token
```

Un flag important de cette commande est `--repository`, qui permet d'indiquer le type de dépôt pour lequel créer le jeton de pull. Par exemple, `--repository=apk` associe l'identité du jeton de pull au rôle `apk.pull`, ce qui lui permet de télécharger des paquets depuis le dépôt APK privé de l'organisation parente.

Pour configurer un credential helper Docker, qui utilise un jeton pour récupérer les images lorsque vous utilisez Docker, exécutez :

```shell
chainctl auth configure-docker
```

> **Remarque** : {{< blurb/noproxy >}}

## Mettre à jour chainctl vers la dernière version

Pour savoir quelle version de `chainctl` est installée, exécutez :

```shell
chainctl version
```

Pour mettre à jour votre installation de `chainctl`, exécutez :

```shell
chainctl update
```

Comme cette commande remplace le binaire installé, vous devez disposer d'un accès en écriture au répertoire où se trouve `chainctl`. Sous Linux et macOS, la mise à jour d'une installation à l'échelle du système, par exemple dans `/usr/local/bin`, nécessite des privilèges d'administrateur (par exemple avec `sudo`). La commande vérifie aussi la signature du binaire téléchargé avant de l'installer ; pour en savoir plus, consultez [Mettre à jour chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

## Configurer chainctl

`chainctl` est livré avec une configuration par défaut, mais certains de ses aspects sont modifiables. Vous pouvez par exemple définir l'emplacement du registre utilisé lorsqu'une commande n'en précise aucun. Pour modifier la configuration actuelle, exécutez :

```shell
chainctl config edit
```

Si vous faites une erreur et ne vous souvenez plus des paramètres d'origine, rétablissez la configuration par défaut avec :

```shell
chainctl config reset
```

Pour en savoir plus, consultez [Gérer la configuration de chainctl](/platform/chainctl-usage/manage-chainctl-config/).

## Lister les images disponibles

Pour voir quelles images Chainguard Containers sont disponibles pour votre compte, exécutez :

```shell
chainctl images list
```

Attention : la génération de cette liste peut prendre un certain temps, et la liste risque de défiler rapidement dans votre terminal.

## Comparer deux versions d'une image

Supposons que vous vouliez comparer deux versions d'une image pour le même paquet. Vous devez connaître l'URL de votre dépôt, le nom de l'image et les deux versions à comparer. Comme versions, vous pouvez utiliser des numéros de version comme `8.12.0`, ou bien `latest` ou `latest-dev`.

Exécutez la commande suivante. Elle utilise le dépôt de l'équipe Chainguard Developer Education, et les deux occurrences de `<image_name>` sont identiques :

```shell
chainctl images diff cgr.dev/chainguard.edu/$IMAGENAME:latest cgr.dev/chainguard.edu/$IMAGENAME:latest-dev
```

Si l'image ou la version demandée n'est pas disponible dans le dépôt que vous utilisez, la commande renvoie une erreur `Forbidden`, comme lorsque vous essayez de récupérer une image à laquelle vous n'avez pas accès ou depuis un dépôt que votre compte n'est pas autorisé à utiliser.

Pour en savoir plus, consultez [Comparer des images Chainguard Containers avec chainctl](/platform/chainctl-usage/comparing-images/).

## Lister les versions de paquets disponibles

Pour obtenir des informations sur les différentes versions de paquets disponibles pour les images, exécutez :

```shell
chainctl packages versions list $PACKAGENAME
```

La commande liste toutes les versions que Chainguard a construites, avec la date de fin de vie de chaque version qui en a une. Elle liste aussi les anciennes versions de paquets qui ne sont plus disponibles.

## Formats de sortie

Les commandes ont parfois un format de sortie par défaut, mais rien ne vous oblige à le conserver. Une option permet d'indiquer à `chainctl` le format de sortie à utiliser, comme ceci :

```shell
chainctl $COMMAND -o $FORMAT
```

L'option `-o` est suivie de l'une des chaînes suivantes : `csv`, `id`, `json`, `none`, `table`, `terse`, `tree` ou `wide`.

Tous les formats de sortie ne conviennent pas à toutes les commandes : testez-les soigneusement avant d'utiliser un format précis dans une automatisation.
