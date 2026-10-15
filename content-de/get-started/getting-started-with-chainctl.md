---
title: "Erste Schritte mit chainctl"
lead: "Mit der chainctl-CLI von Chainguard verwalten Sie Container-Images und IAM-Ressourcen sicherer über die Befehlszeile – für DevOps- und Security-Workflows."
description: "Erste Schritte mit den Grundlagen von chainctl: Authentifizierung, Verwaltung von Organisationen und die wichtigsten Befehle der Container-Security-Plattform von Chainguard"
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

Mit `chainctl` von Chainguard verwalten Sie Container-Images, Identitätsressourcen und Sicherheitskonfigurationen in Ihrer gesamten Organisation über die Befehlszeile. Dieser Leitfaden stellt die wichtigsten Befehle vor, mit denen Sie `chainctl` effektiv in Ihren Security- und DevOps-Workflows einsetzen. Die vollständige Befehlsdokumentation finden Sie in der [chainctl-Referenz](/platform/chainctl/).

## Authentifizieren und Authentifizierungsstatus prüfen

Bevor Sie `chainctl` verwenden können, müssen Sie sich zuerst [bei der Chainguard-Plattform authentifizieren](/chainguard/containers/registry/authenticating/). Führen Sie dazu Folgendes aus:

```shell
chainctl auth login
```

Daraufhin erscheint eine Liste von Identitätsanbietern, aus der Sie einen auswählen. Verwenden Sie den Anbieter, der mit Ihrem Chainguard-Konto verknüpft ist. Sobald Sie einen ausgewählt haben, zum Beispiel Google, öffnet `chainctl` ein Browserfenster, in dem Sie sich mit Ihren Zugangsdaten anmelden. Nach erfolgreicher Anmeldung können Sie diesen Identitätsanbieter als Standard für künftige Anmeldungen speichern. Anschließend wird ein Token ausgetauscht, und Sie können `chainctl` verwenden.

{{< blurb/chainctl-auth >}}

Um Ihren Authentifizierungsstatus jederzeit zu prüfen, geben Sie Folgendes ein:

```shell
chainctl auth status
```

Dieser Befehl listet Ihre Identität und weitere mit Ihrem Konto verknüpfte Attribute auf, darunter die Ihrem Konto zugewiesenen Rollen und Capabilities.

Um ein Pull-Token zu erstellen, verwenden Sie:

```shell
chainctl auth pull-token
```

Ein wichtiges Flag für diesen Befehl ist `--repository`. Damit legen Sie den Repository-Typ fest, für den das Pull-Token erstellt wird. Mit `--repository=apk` binden Sie die Pull-Token-Identität beispielsweise an die Rolle `apk.pull`, sodass die Identität Pakete aus dem privaten APK-Repository der übergeordneten Organisation herunterladen kann.

Um einen Docker-Credential-Helper zu konfigurieren, der beim Arbeiten mit Docker ein Token zum Pullen von Images verwendet, nutzen Sie:

```shell
chainctl auth configure-docker
```

> **Hinweis**: {{< blurb/noproxy >}}

## chainctl auf die neueste Version aktualisieren

Um zu sehen, welche `chainctl`-Version installiert ist, verwenden Sie:

```shell
chainctl version
```

Um Ihre `chainctl`-Installation zu aktualisieren, verwenden Sie:

```shell
chainctl update
```

Da dieser Befehl die installierte Binärdatei ersetzt, benötigen Sie Schreibzugriff auf das Verzeichnis, in dem `chainctl` liegt. Unter Linux und macOS erfordert die Aktualisierung einer systemweiten Installation, etwa in `/usr/local/bin`, Administratorrechte (zum Beispiel mit `sudo`). Der Befehl verifiziert außerdem vor der Installation die Signatur der heruntergeladenen Binärdatei im laufenden Prozess. Details finden Sie unter [chainctl aktualisieren](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

## chainctl konfigurieren

`chainctl` wird mit einer Standardkonfiguration ausgeliefert, von der sich aber einige Aspekte anpassen lassen. Sie können zum Beispiel festlegen, welcher Registry-Standort verwendet wird, wenn ein Befehl keinen angibt. Um die aktuelle Konfiguration zu bearbeiten, verwenden Sie:

```shell
chainctl config edit
```

Wenn Ihnen ein Fehler unterläuft und Sie sich nicht mehr an die ursprünglichen Einstellungen erinnern, setzen Sie die Konfiguration mit folgendem Befehl auf die Standardwerte zurück:

```shell
chainctl config reset
```

Mehr dazu erfahren Sie unter [chainctl-Konfiguration verwalten](/platform/chainctl-usage/manage-chainctl-config/).

## Verfügbare Images auflisten

Um zu sehen, welche Chainguard Containers für Ihr Konto verfügbar sind, verwenden Sie:

```shell
chainctl images list
```

Seien Sie gewarnt: Das Erstellen der Liste kann eine Weile dauern, und sie läuft im Terminal vermutlich schnell durch.

## Zwei Image-Versionen vergleichen

Angenommen, Sie möchten zwei Versionen eines Images für dasselbe Paket vergleichen. Dafür brauchen Sie die URL Ihres Repositorys, den Image-Namen und die beiden Versionen, die Sie vergleichen möchten. Als Versionen können Sie Release-Nummern wie `8.12.0` oder `latest` bzw. `latest-dev` verwenden.

Verwenden Sie den folgenden Befehl. Er zeigt das Repository unseres Chainguard-Developer-Education-Teams, und beide Vorkommen von `<image_name>` sind identisch:

```shell
chainctl images diff cgr.dev/chainguard.edu/$IMAGENAME:latest cgr.dev/chainguard.edu/$IMAGENAME:latest-dev
```

Ist ein angefordertes Image oder Release in dem von Ihnen verwendeten Repository nicht verfügbar, gibt der Befehl einen `Forbidden`-Fehler zurück – genau wie beim Versuch, ein Image zu pullen, auf das Sie keinen Zugriff haben, oder aus einem Repository zu pullen, für das Ihr Konto nicht berechtigt ist.

Mehr dazu erfahren Sie unter [Chainguard Containers mit chainctl vergleichen](/platform/chainctl-usage/comparing-images/).

## Verfügbare Paketversionen auflisten

Um Details zu den verschiedenen Paketversionen abzurufen, die in Images verwendet werden können, verwenden Sie:

```shell
chainctl packages versions list $PACKAGENAME
```

Dieser Befehl listet alle Versionen auf, die Chainguard gebaut hat, sowie das End-of-Life-Datum jeder Version, der eines zugewiesen ist. Außerdem listet er ältere Paketversionen auf, die nicht mehr verfügbar sind.

## Ausgabeformate

Befehle haben möglicherweise ein Standardformat für die Ausgabe, aber daran müssen Sie sich nicht halten. Mit einer Option teilen Sie `chainctl` mit, welches Ausgabeformat es verwenden soll:

```shell
chainctl $COMMAND -o $FORMAT
```

Auf `-o` folgt einer dieser Werte: `csv`, `id`, `json`, `none`, `table`, `terse`, `tree` oder `wide`.

Nicht jedes Ausgabeformat ist für jeden Befehl sinnvoll. Testen Sie daher gründlich, bevor Sie ein bestimmtes Format in der Automatisierung einsetzen.
