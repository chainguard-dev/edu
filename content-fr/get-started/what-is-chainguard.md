---
title: "Qu'est-ce que Chainguard ?"
linktitle: "Qu'est-ce que Chainguard ?"
lead: "Une présentation générale de Chainguard : le problème que l'entreprise résout, les produits qu'elle propose et ce qui les distingue."
description: "Une présentation de Chainguard : sa mission, être la source sécurisée de l'open source, ses produits (Containers, Libraries et OS) et la Factory qui les construit."
type: "article"
date: 2026-07-23T00:00:00+00:00
lastmod: 2026-10-14T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 10
translation:
  sourceLastmod: 2026-09-28T14:00:04+00:00
  reviewed: false
---

Presque toutes les applications modernes reposent sur des logiciels open source. Ces logiciels sont puissants, mais ils posent des problèmes : des vulnérabilités (dont des CVE divulguées publiquement), des dépendances non corrigées, une provenance incertaine et un travail incessant pour tout maintenir à jour. Suivre et corriger ces problèmes dans une base de code étendue mobilise un temps d'ingénierie qui pourrait servir à développer des produits.

La mission de Chainguard est d'être la source sécurisée de l'open source. Plutôt que de vous laisser corriger et renforcer vous-même les logiciels open source, Chainguard les reconstruit à partir des sources dans un environnement de build renforcé, les maintient à jour en continu et les distribue avec les métadonnées dont vous avez besoin pour vérifier ce que vous exécutez. Résultat : des logiciels qui présentent peu ou pas de CVE connues et qui demandent beaucoup moins de travail de correction à votre équipe.

## Ce que propose Chainguard

Chainguard reconstruit des logiciels open source sous forme de produits que vous pouvez adopter directement, selon la façon dont vous consommez vos dépendances :

- **[Chainguard Containers](/chainguard/containers/overview/)** sont des images de conteneur minimales et renforcées. Selon une philosophie distroless, chaque image ne contient que votre application et ses dépendances d'exécution essentielles, ce qui réduit au minimum la surface d'attaque globale. Ce minimalisme explique en grande partie pourquoi elles présentent [peu ou pas de CVE](/chainguard/containers/concepts/zerocve/).
- **[Chainguard Libraries](/chainguard/libraries/introduction/overview/)** appliquent la même approche aux dépendances des langages. Ce sont des remplacements directs des paquets open source des écosystèmes Java, Python et JavaScript, reconstruits à partir de sources vérifiées et surveillés en continu.

Vous récupérez Chainguard Containers et Chainguard Libraries depuis un point d'accès unique qui applique vos politiques : le [Chainguard Repository](/chainguard/chainguard-repository/overview/).

La plupart des équipes commencent par Containers et Libraries, mais Chainguard sécurise bien plus que cela. Ses autres produits comprennent :

- **[Chainguard OS](/chainguard/chainguard-os/overview/)**, la base Linux renforcée sur laquelle reposent les autres produits.
- **[Chainguard VMs](/chainguard/vms/overview/)**, des images de machines virtuelles minimales pour les charges de travail dans le cloud et sur hyperviseur.
- **[Chainguard Actions](/chainguard/actions/overview/)**, des remplacements renforcés pour les GitHub Actions populaires.
- **[Guardener](/chainguard/guardener/)**, des outils pour renforcer votre propre code source.
- **[Chainguard Agent Skills](/chainguard/agent-skills/overview/)**, des skills pour agents d'IA dont la sécurité a été vérifiée.

## La Chainguard Factory

Derrière ces produits se trouve la [Chainguard Factory](/platform/factory/overview/), le système de build automatisé au cœur de l'activité de Chainguard. La Factory surveille en continu des milliers de projets open source. Lorsqu'une nouvelle version upstream paraît, elle récupère le code source, le vérifie, le reconstruit, le teste à nouveau, puis publie des paquets signés construits à partir des sources, accompagnés de SBOM et de métadonnées de provenance.

Comme la Factory fait ce travail pour vous, adopter un artefact Chainguard réduit immédiatement le risque lié à votre chaîne d'approvisionnement logicielle. Comme Chainguard maintient l'artefact en continu, ces gains de sécurité se prolongent dans le temps, avec un minimum de changements dans vos workflows existants.

## Pourquoi Chainguard

Par rapport aux artefacts issus de dépôts publics, Chainguard vous apporte :

- **Peu ou pas de CVE**, pour que votre équipe passe moins de temps à trier et à corriger des vulnérabilités.
- **Une surface d'attaque minimale**, car les artefacts ne contiennent que ce dont ils ont besoin pour s'exécuter.
- **Une provenance vérifiable** grâce aux signatures, aux SBOM et aux builds à partir des sources, pour que vous puissiez prouver ce que contient votre chaîne d'approvisionnement logicielle.
- **Des mises à jour continues**, pour que les correctifs arrivent automatiquement au lieu d'attendre des mises à niveau manuelles.

## Pour aller plus loin

- Prêt à essayer une image ? Suivez un [exemple de conteneur](/get-started/containers-examples/) pour votre langage ou votre service.
- Vous remplacez plutôt des dépendances ? Commencez par l'[introduction aux bibliothèques](/get-started/libraries-examples/).
- Vous transférez des charges de travail existantes ? Suivez les [guides de migration](/get-started/migration/).
- Vous déployez Chainguard auprès de vos équipes ? Découvrez comment [intégrer vos équipes](/get-started/onboard-your-teams/).
