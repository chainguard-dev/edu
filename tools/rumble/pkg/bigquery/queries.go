/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cgbigquery

const (
	summaryTable = "`cloudevents_grype_scan_results.rumble_summary`"

	LegacyCsvHeader = `f0_,image,scanner,time,low_cve_cnt,med_cve_cnt,high_cve_cnt,crit_cve_cnt,unknown_cve_cnt,tot_cve_cnt,digest`

	LegacyCsvQuery = `
SELECT
	ROW_NUMBER() OVER (ORDER BY time),
	image,
    tags,
	scanner,
	FORMAT_DATETIME("%Y-%m-%d %H:%M:%S", DATE(time)) as time,
	low_cve_count as low_cve_cnt,
	med_cve_count as med_cve_cnt,
	high_cve_count as high_cve_cnt,
	crit_cve_count as crit_cve_cnt,
	unknown_cve_count as unknown_cve_cnt,
	low_cve_count + med_cve_count + high_cve_count + crit_cve_count + unknown_cve_count AS tot_cve_cnt,
	digest
FROM ` + summaryTable + `
WHERE tags NOT LIKE '%latest-dev%'
AND time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 31 DAY)
AND (image NOT LIKE 'cgr.dev%%' OR image LIKE 'cgr.dev/chainguard/%%')`
)
