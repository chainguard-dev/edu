---
title: "Support erhalten"
linktitle: "Support erhalten"
lead: "Chainguard bietet mehrere Wege, Hilfe zu erhalten, und welcher der richtige ist, hängt von Ihrer Situation ab. Dieser Leitfaden zeigt, was Sie zuerst prüfen sollten, welcher Kanal für Ihr Anliegen zuständig ist und wie Sie bei Bedarf ein Support-Ticket eröffnen."
description: "Hilfe von Chainguard erhalten: Self-Service-Angebote prüfen, den richtigen Support-Kanal wählen und ein Ticket eröffnen, mit dem ein Support-Engineer direkt arbeiten kann."
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

Wenn die Dokumentation Ihre Frage nicht beantwortet, bietet Chainguard mehrere Wege, Hilfe zu erhalten. Dieser Leitfaden zeigt, was Sie zuerst prüfen sollten, welcher Kanal für Ihr Anliegen zuständig ist und wie Sie bei Bedarf ein Support-Ticket eröffnen.

## Vor dem Eröffnen eines Tickets

Auf viele Fragen gibt es bereits eine veröffentlichte Antwort, die Sie in Sekunden finden:

- **Diese Dokumentationsseite.** Suchen Sie über das Suchfeld oben auf jeder Seite.

- **KI fragen.** Klicken Sie oben rechts auf einer beliebigen Seite dieser Website auf **KI fragen** und stellen Sie Ihre Frage in natürlicher Sprache. Der Assistent stützt sich auf die Dokumentation und die Support-Inhalte von Chainguard und nennt seine Quellen. Prüfen Sie die Antwort und ihre Quellen, bevor Sie danach handeln.

- **Die [Chainguard-Wissensdatenbank](https://support.chainguard.dev/hc/en-us).** Dort veröffentlichen die Support-Engineers von Chainguard Artikel zu Problemen, die immer wieder auftreten.

## Wohin Sie Ihre Anfrage senden

Das Support-Portal bearbeitet die meisten Anfragen, ist aber nicht der einzige Weg und in manchen Situationen nicht der richtige. Suchen Sie Ihre Situation in der folgenden Liste:

- **Sie haben ein Problem mit einem Chainguard-Produkt oder mit der Konfiguration Ihrer Organisation.** Eröffnen Sie ein Ticket im [Support-Portal](https://support.chainguard.dev/).

- **Sie möchten Ihre Multi-Faktor-Authentifizierung auf ein neues Gerät übertragen, oder Sie haben das Gerät mit Ihrer Authenticator-App verloren.** Wo Sie das ändern, hängt davon ab, wie Sie sich anmelden, und bei den meisten Anmeldewegen verwaltet nicht Chainguard Ihre MFA. Siehe [MFA-Gerät ändern oder zurücksetzen](/get-started/mfa-devices/).

- **Sie können sich überhaupt nicht anmelden und erreichen deshalb das Portal nicht.** Schreiben Sie eine E-Mail an [support@chainguard.dev](mailto:support@chainguard.dev).

- **Ihre Organisation nutzt Catalog Starter.** Nutzen Sie die [Wissensdatenbank](https://support.chainguard.dev/hc/en-us), den [Community-Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw) und die kostenlosen [Chainguard-Kurse](https://courses.chainguard.dev/). Catalog Starter umfasst keinen Zugang zu Tickets.

- **Ihre Anfrage betrifft Ihr Abonnement oder das, wofür Ihre Organisation lizenziert ist – zum Beispiel, ob ein bestimmtes Image in Ihren Entitlements enthalten ist.** Wenden Sie sich an Ihr Account-Team, also an den Customer Success Manager oder den Solutions Architect, der Ihrer Organisation zugeordnet ist.

- **Sie können ein Container-Image oder eine bestimmte Version davon nicht pullen.** Arbeiten Sie zuerst [Probleme mit der Verfügbarkeit von Containern und Versionen beheben](/chainguard/containers/troubleshooting/container-version-troubleshooting/) durch. Dort erfahren Sie, welche Fälle Sie selbst lösen können und für welche Sie ein Ticket brauchen.

## Ticket eröffnen

### Zugang zum Portal sicherstellen

Für das Support-Portal gelten zwei Voraussetzungen.

Erstens braucht Ihre Organisation einen kostenpflichtigen Plan. Catalog Starter umfasst weder Support-Tickets noch Ursachenanalysen. Was der kostenlose Plan abdeckt, erfahren Sie unter [Chainguard Catalog Starter](/chainguard/containers/reference/catalog-starter/).

Zweitens muss Ihre Identität mit einer Organisation verknüpft sein. Das Portal identifiziert Sie über Ihr Konto in der Chainguard Console, und eine nicht verknüpfte Identität führt zu einem Fehler. Melden Sie sich zur Prüfung in der [Chainguard Console](https://console.chainguard.dev) an und suchen Sie Ihre Organisation in der linken Seitenleiste. Fehlt sie dort, bitten Sie eine Administratorin oder einen Administrator Ihrer Organisation, Sie einzuladen. Öffnen Sie dann die Einladungs-E-Mail und schließen Sie die Einrichtung ab. Wenn Sie sich anmelden, ohne die Einrichtung abzuschließen, bleibt Ihre Identität unverknüpft.

{{< note >}}
Administratoren können Benutzer in der Console unter **Settings > Users > Invite users** oder über die Befehlszeile einladen. Siehe [IAM-Organisationen in Chainguard verwalten](/platform/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/).
{{< /note >}}

### Anfrage einreichen

1. Melden Sie sich in der [Chainguard Console](https://console.chainguard.dev) an.

1. Klicken Sie in der linken Seitenleiste auf **Support**. Sie können auch direkt [support.chainguard.dev](https://support.chainguard.dev/) aufrufen.

1. Füllen Sie das Anfrageformular aus. Vor dem Absenden schlägt Ihnen das Portal passende Dokumentation und eine generierte Antwort vor. Wenn das Ihre Frage klärt, sind Sie fertig. Andernfalls reichen Sie die Anfrage wie gewohnt ein.

### Wenn das Portal einen Fehler meldet

Gehen Sie die folgenden Schritte durch:

1. Öffnen Sie die Console und das Support-Portal in einem privaten Browserfenster.

1. Löschen Sie den Cache und die Cookies Ihres Browsers.

1. Vergewissern Sie sich, dass Sie sich mit derselben Identität anmelden, mit der Sie eingeladen wurden.

Bleibt der Fehler bestehen, schreiben Sie eine E-Mail an [support@chainguard.dev](mailto:support@chainguard.dev) mit einem Screenshot des Fehlers, der E-Mail-Adresse des Kontos, das Sie verwenden möchten, und dem Einladungslink, falls Sie ihn noch haben.

## Was Ihre Anfrage enthalten sollte

Ein Support-Engineer kann direkt mit der Arbeit an einem Problem beginnen, statt Sie um weitere Informationen zu bitten, wenn Ihre Anfrage Folgendes enthält:

- Den Namen Ihrer Organisation.

- Den Namen und das Tag des Images oder Pakets sowie den Digest, falls vorhanden.

- Den ausgeführten Befehl und seine vollständige Ausgabe, einschließlich aller Fehlermeldungen.

- Die `chainctl`-Version, falls das Problem das Befehlszeilen-Tool betrifft. Führen Sie `chainctl version` aus, um sie zu ermitteln.

- Was Sie stattdessen erwartet haben.

- Alles Weitere, was Ihrer Meinung nach helfen könnte: Logs, Screenshots oder eine kurze Bildschirmaufnahme.
