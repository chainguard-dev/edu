---
title: "Obtenir de l'assistance"
linktitle: "Obtenir de l'assistance"
lead: "Chainguard propose plusieurs façons d'obtenir de l'aide, et la bonne dépend de votre situation. Ce guide explique ce qu'il faut vérifier en premier, quel canal traite votre type de demande et comment ouvrir un ticket d'assistance si nécessaire."
description: "Obtenez de l'aide auprès de Chainguard : consultez les ressources en libre-service, choisissez le bon canal d'assistance et ouvrez un ticket qu'un ingénieur support peut traiter."
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

Lorsque la documentation ne répond pas à votre question, Chainguard propose plusieurs façons d'obtenir de l'aide. Ce guide explique ce qu'il faut vérifier en premier, quel canal traite votre type de demande et comment ouvrir un ticket d'assistance si nécessaire.

## Avant d'ouvrir un ticket

Beaucoup de questions ont déjà une réponse publiée, que vous trouvez en quelques secondes :

- **Ce site de documentation.** Lancez une recherche depuis le champ situé en haut de chaque page.

- **Demander à l'IA.** Cliquez sur **Demander à l'IA** dans l'angle supérieur droit de n'importe quelle page de ce site et posez votre question en langage courant. L'assistant s'appuie sur la documentation et les contenus d'assistance de Chainguard, et cite ses sources. Vérifiez la réponse et ses sources avant d'agir.

- **La [base de connaissances Chainguard](https://support.chainguard.dev/hc/en-us).** Les ingénieurs support de Chainguard y publient des articles sur les problèmes récurrents.

## Où envoyer votre demande

Le portail d'assistance traite la plupart des demandes, mais ce n'est pas la seule voie et, dans certaines situations, ce n'est pas la bonne. Trouvez votre situation dans la liste suivante :

- **Vous rencontrez un problème avec un produit Chainguard ou avec la configuration de votre organisation.** Ouvrez un ticket sur le [portail d'assistance](https://support.chainguard.dev/).

- **Vous devez transférer votre authentification multifacteur sur un nouvel appareil, ou vous avez perdu l'appareil sur lequel se trouve votre application d'authentification.** L'endroit où effectuer ce changement dépend de votre mode de connexion et, pour la plupart des modes de connexion, ce n'est pas Chainguard qui gère votre MFA. Consultez [Changer ou réinitialiser votre appareil MFA](/get-started/mfa-devices/).

- **Vous ne parvenez pas du tout à vous connecter, et vous n'avez donc pas accès au portail.** Écrivez à [support@chainguard.dev](mailto:support@chainguard.dev).

- **Votre organisation utilise Catalog Starter.** Utilisez la [base de connaissances](https://support.chainguard.dev/hc/en-us), le [Slack de la communauté](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw) et les [cours Chainguard](https://courses.chainguard.dev/) gratuits. Catalog Starter n'inclut pas l'accès aux tickets.

- **Votre demande concerne votre abonnement ou ce que couvre la licence de votre organisation, par exemple si une image donnée fait partie de vos droits d'accès.** Contactez votre équipe de compte, c'est-à-dire le customer success manager ou le solutions architect affecté à votre organisation.

- **Vous ne parvenez pas à récupérer une image de conteneur ou une version précise d'une image.** Suivez d'abord [Résoudre les problèmes de disponibilité des conteneurs et des versions](/chainguard/containers/troubleshooting/container-version-troubleshooting/). Ce guide vous indique les cas que vous pouvez résoudre vous-même et ceux qui nécessitent un ticket.

## Ouvrir un ticket

### Vérifier que vous avez accès au portail

Le portail d'assistance a deux prérequis.

Premièrement, votre organisation doit disposer d'un forfait payant. Catalog Starter n'inclut ni les tickets d'assistance ni l'analyse des causes profondes. Pour savoir ce que couvre le forfait gratuit, consultez [Chainguard Catalog Starter](/chainguard/containers/reference/catalog-starter/).

Deuxièmement, votre identité doit être associée à une organisation. Le portail vous identifie par votre compte Chainguard Console, et une identité non associée provoque une erreur. Pour le vérifier, connectez-vous à la [Chainguard Console](https://console.chainguard.dev) et cherchez votre organisation dans la barre latérale gauche. Si elle n'y figure pas, demandez à un administrateur de votre organisation de vous inviter, puis ouvrez l'e-mail d'invitation et terminez la procédure de configuration. Si vous vous connectez sans terminer cette procédure, votre identité reste non associée.

{{< note >}}
Les administrateurs peuvent inviter des utilisateurs depuis la Console, sous **Settings > Users > Invite users**, ou depuis la ligne de commande. Consultez [Gérer les organisations IAM dans Chainguard](/platform/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/).
{{< /note >}}

### Envoyer la demande

1. Connectez-vous à la [Chainguard Console](https://console.chainguard.dev).

1. Dans la barre latérale gauche, cliquez sur **Support**. Vous pouvez aussi accéder directement à [support.chainguard.dev](https://support.chainguard.dev/).

1. Remplissez le formulaire de demande. Avant l'envoi, le portail vous propose de la documentation pertinente et une réponse générée. Si elle répond à votre question, vous avez terminé. Sinon, envoyez la demande normalement.

### Si le portail renvoie une erreur

Suivez les étapes suivantes :

1. Ouvrez la Console et le portail d'assistance dans une fenêtre de navigation privée.

1. Videz le cache et les cookies de votre navigateur.

1. Vérifiez que vous vous connectez avec la même identité que celle avec laquelle vous avez été invité.

Si l'erreur persiste, écrivez à [support@chainguard.dev](mailto:support@chainguard.dev) en joignant une capture d'écran de l'erreur, l'adresse e-mail du compte que vous essayez d'utiliser et le lien d'invitation si vous l'avez encore.

## Ce que doit contenir votre demande

Un ingénieur support peut s'attaquer directement au problème, sans vous demander d'informations complémentaires, si votre demande contient :

- Le nom de votre organisation.

- Le nom et le tag de l'image ou du paquet, ainsi que le digest si vous l'avez.

- La commande que vous avez exécutée et sa sortie complète, y compris les éventuels messages d'erreur.

- La version de `chainctl`, si le problème concerne l'outil en ligne de commande. Exécutez `chainctl version` pour l'obtenir.

- Ce que vous attendiez à la place.

- Tout autre élément qui pourrait aider : logs, captures d'écran ou un court enregistrement d'écran.
