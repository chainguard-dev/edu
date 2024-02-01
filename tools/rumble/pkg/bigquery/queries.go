/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cgbigquery

const (
	LegacyCsvHeader    = `f0_,image,scanner,scanner_version,scanner_db_version,time,low_cve_cnt,med_cve_cnt,high_cve_cnt,crit_cve_cnt,unknown_cve_cnt,tot_cve_cnt,digest`
	ImageScanCsvHeader = `image,package,vulnerability,version,type,s`

	AllVulnsQuery = `
SELECT DISTINCT vulnerability
FROM insights_ds.vulnerabilities
`

	AffectedImagesQuery = `
SELECT s1.image, s1.time as time,
FROM insights_ds.vulnerabilities
AS s2
INNER JOIN ` + "`" + `insights_ds.image-scan-summary` + "`" + `
AS s1
ON s1.id = s2.scan_id
WHERE s2.vulnerability = @vulnerability
AND s1.image NOT LIKE "cgr.dev/chainguard-private/%"
AND s1.image NOT LIKE "cgr.dev/custom%"
GROUP BY s1.time, s1.image
ORDER BY s1.image, s1.time
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
FROM ` + "`" + `insights_ds.image-scan-summary` + "`" + `
WHERE DATE(time) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()
AND scanner = "grype"
AND image NOT LIKE "cgr.dev/chainguard-private/%"
AND image NOT LIKE "cgr.dev/custom%"
`

	ImageComparisonCsvQuery = `
WITH ruuuumble AS (
	SELECT s1.image,
		s1.time as t,
		s2.name as package,
		s2.vulnerability,
		s2.installed as version,
		s2.type,
		s2.severity
	FROM insights_ds.vulnerabilities
	AS s2
	INNER JOIN ` + "`" + "insights_ds.image-scan-summary" + "`" + `
	AS s1
	ON s1.id = s2.scan_id
	WHERE s1.image = @theirs
	OR s1.image = @ours
	)
	SELECT image, package, vulnerability, version, type, severity FROM ruuuumble
	WHERE DATE(t) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()
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
