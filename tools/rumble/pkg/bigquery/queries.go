/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cgbigquery

const (
	vulnsTable   = "`cloudevents_grype_scan_results.rumble_vulns`"
	summaryTable = "`cloudevents_grype_scan_results.rumble_summary`"

	LegacyCsvHeader    = `f0_,image,scanner,scanner_version,scanner_db_version,time,low_cve_cnt,med_cve_cnt,high_cve_cnt,crit_cve_cnt,unknown_cve_cnt,tot_cve_cnt,digest`
	ImageScanCsvHeader = `image,package,vulnerability,version,type,s`

	AllVulnsQuery = `
SELECT DISTINCT vulnerability
FROM ` + vulnsTable

	AffectedImagesQuery = `
SELECT summ.image, summ.time as time,
FROM ` + vulnsTable + ` AS vulns
INNER JOIN ` + summaryTable + ` AS scan
ON scan.id = vulns.scan_id
WHERE vulns.vulnerability = @vulnerability
GROUP BY scan.time, scan.image
ORDER BY scan.image, scan.time
`

	LegacyCsvQuery = `
SELECT
	ROW_NUMBER() OVER (ORDER BY time),
	image,
	scanner,
	scanner_version,
	scanner_db_version,
	FORMAT_DATETIME("%Y-%m-%d %H:%M:%S", DATE(time)) as time,
	low_cve_count as low_cve_cnt,
	med_cve_count as med_cve_cnt,
	high_cve_count as high_cve_cnt,
	crit_cve_count as crit_cve_cnt,
	unknown_cve_count as unknown_cve_cnt,
	low_cve_count + med_cve_count + high_cve_count + crit_cve_count + unknown_cve_count AS tot_cve_cnt,
	digest
FROM ` + summaryTable

	ImageComparisonCsvQuery = `
WITH ruuuumble AS (
	SELECT scan.image,
		scan.time as t,
		vulns.name as package,
		vulns.vulnerability,
		vulns.installed as version,
		vulns.type,
		vulns.severity
	FROM ` + vulnsTable + ` AS vulns
	INNER JOIN ` + summaryTable + ` AS scan ON scan.id = vulns.scan_id
	WHERE (scan.image = @theirs AND scan.tags = @their_tag)
	OR (scan.image = @ours AND scan.tags = @our_tag)
	)
	SELECT image, package, vulnerability, version, type, severity FROM ruuuumble
	GROUP BY vulnerability, image, package, version, type, severity
	ORDER BY (
	CASE WHEN severity = "Critical" THEN 1
		WHEN severity = "High" THEN 2
		WHEN severity = "Medium" THEN 3
		WHEN severity = "Low" THEN 4
		WHEN severity = "Negligible" THEN 5
		WHEN severity = "Unknown" THEN 6
		ELSE 7
	END
	)
`
)
