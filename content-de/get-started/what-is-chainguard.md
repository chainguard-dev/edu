---
title: "Was ist Chainguard?"
linktitle: "Was ist Chainguard?"
lead: "Eine Einführung in Chainguard: welches Problem Chainguard löst, welche Produkte es anbietet und was sie auszeichnet."
description: "Ein Überblick über Chainguard: die Mission, die sichere Quelle für Open Source zu sein, die Produkte (Containers, Libraries und OS) und die Factory, die sie baut."
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

Fast jede moderne Anwendung basiert auf Open-Source-Software. Diese Software ist leistungsfähig, bringt aber Probleme mit sich: Schwachstellen (einschließlich öffentlich bekannter CVEs), ungepatchte Abhängigkeiten, unklare Herkunft und den ständigen Aufwand, alles auf dem aktuellen Stand zu halten. Diese Probleme in einer großen Codebasis zu verfolgen und zu beheben, kostet Entwicklungszeit, die in die Produktentwicklung fließen könnte.

Chainguards Mission ist es, die sichere Quelle für Open Source zu sein. Statt Ihnen das Patchen und Härten von Open-Source-Software zu überlassen, baut Chainguard sie in einer gehärteten Build-Umgebung aus dem Quellcode neu, hält sie kontinuierlich aktuell und liefert sie mit den Metadaten aus, die Sie brauchen, um zu verifizieren, was Sie ausführen. Das Ergebnis ist Software mit wenigen bis gar keinen bekannten CVEs, die Ihrem Team deutlich weniger Aufwand bei der Behebung abverlangt.

## Was Chainguard anbietet

Chainguard baut Open-Source-Software neu und macht daraus Produkte, die Sie direkt einsetzen können – je nachdem, wie Sie Abhängigkeiten beziehen:

- **[Chainguard Containers](/chainguard/containers/overview/)** ist eine Sammlung minimaler, gehärteter Container-Images. Nach dem Distroless-Prinzip enthält jedes Image nur Ihre Anwendung und deren unverzichtbare Laufzeitabhängigkeiten, was die Angriffsfläche insgesamt minimiert. Diese Minimalität ist ein wesentlicher Grund dafür, dass sie [wenige bis gar keine CVEs](/chainguard/containers/concepts/zerocve/) aufweisen.
- **[Chainguard Libraries](/chainguard/libraries/introduction/overview/)** übertragen denselben Ansatz auf Sprachabhängigkeiten. Sie sind Drop-in-Ersatz für Open-Source-Pakete in den Ökosystemen Java, Python und JavaScript, aus verifizierten Quellen neu gebaut und kontinuierlich überwacht.

Sie pullen Chainguard Containers und Libraries von einem einzigen Endpunkt, der Richtlinien berücksichtigt: dem [Chainguard Repository](/chainguard/chainguard-repository/overview/).

Mit Containers und Libraries beginnen die meisten Teams, aber Chainguard sichert noch mehr ab. Zu den weiteren Produkten gehören:

- **[Chainguard OS](/chainguard/chainguard-os/overview/)**, die gehärtete Linux-Grundlage, auf der die anderen Produkte aufbauen.
- **[Chainguard VMs](/chainguard/vms/overview/)**, minimale Images für virtuelle Maschinen in Cloud- und Hypervisor-Umgebungen.
- **[Chainguard Actions](/chainguard/actions/overview/)**, gehärteter Ersatz für beliebte GitHub Actions.
- **[Guardener](/chainguard/guardener/)**, Werkzeuge zum Härten Ihres eigenen Quellcodes.
- **[Chainguard Agent Skills](/chainguard/agent-skills/overview/)**, sicherheitsgeprüfte Skills für KI-Agenten.
- **[Chainguard Checks](/chainguard/checks/overview/)**, CI für GitHub-Pull-Requests, die jeden Check in einer eigenen isolierten microVM ausführt.
- **[Chainguard Workspaces](/chainguard/workspaces/overview/)**, Remote-Sitzungen in microVMs für Entwicklung und Coding-Agents, die Ihre Anmeldedaten aus der Sitzung heraushalten.

## Die Chainguard Factory

Hinter diesen Produkten steht die [Chainguard Factory](/platform/factory/overview/), das automatisierte Build-System im Zentrum von Chainguards Arbeit. Die Factory überwacht kontinuierlich Tausende von Open-Source-Projekten. Erscheint ein neues Upstream-Release, lädt sie den Quellcode herunter, verifiziert ihn, baut ihn neu, testet ihn erneut und veröffentlicht signierte, aus dem Quellcode gebaute Pakete zusammen mit SBOMs und Provenance-Metadaten.

Da die Factory diese Arbeit für Sie übernimmt, senkt der Einsatz eines Chainguard-Artefakts Ihr Risiko in der Software-Lieferkette sofort. Da Chainguard das Artefakt kontinuierlich pflegt, wirken diese Sicherheitsverbesserungen dauerhaft fort, bei minimalen Änderungen an Ihren bestehenden Workflows.

## Warum Chainguard

Im Vergleich zu Artefakten aus öffentlichen Repositorys bietet Ihnen Chainguard:

- **Wenige bis gar keine CVEs**, sodass Ihr Team weniger Zeit mit der Triage und dem Patchen von Schwachstellen verbringt.
- **Eine minimale Angriffsfläche**, weil Artefakte nur das enthalten, was sie zur Ausführung brauchen.
- **Nachweisbare Herkunft** durch Signaturen, SBOMs und Builds aus dem Quellcode, sodass Sie belegen können, was in Ihrer Software-Lieferkette steckt.
- **Kontinuierliche Updates**, sodass Patches automatisch eintreffen, statt auf manuelle Upgrades zu warten.

## Wie es weitergeht

- Sie möchten ein Image ausprobieren? Arbeiten Sie ein [Container-Beispiel](/get-started/containers-examples/) für Ihre Sprache oder Ihren Service durch.
- Sie möchten stattdessen Abhängigkeiten ersetzen? Beginnen Sie mit dem [Einstieg in Bibliotheken](/get-started/libraries-examples/).
- Sie möchten bestehende Workloads umziehen? Gehen Sie die [Migrationsleitfäden](/get-started/migration/) Schritt für Schritt durch.
- Sie führen Chainguard in Ihren Teams ein? Erfahren Sie, wie Sie [Ihre Teams einbinden](/get-started/onboard-your-teams/).
