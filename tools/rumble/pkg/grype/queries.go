/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package grype

const (
	vulnIDquery = `SELECT DISTINCT id, data_source, severity, description
FROM "vulnerability_metadata"
WHERE id = ?
AND (
	data_source LIKE 'https://nvd.nist.gov/%'
	OR data_source LIKE 'https://github.com/%'
	OR data_source LIKE 'https://linux.oracle.com/%'
	OR data_source LIKE 'https://alas.aws.amazon.com/%'
)`

	// some vulns do not have an nvd URL so use the distro URL
	// e.g. security.debian.org, people.ubuntu.com etc.
	altVulnIDquery = `SELECT DISTINCT id, data_source, severity, description
FROM "vulnerability_metadata"
WHERE id = ?
LIMIT 1`
)
