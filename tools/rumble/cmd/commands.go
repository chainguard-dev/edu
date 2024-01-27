/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cmd

import (
	"github.com/spf13/cobra"
)

// rootCmd represents the base command when called without any subcommands
func New() *cobra.Command {
	o := &options{}
	cmd := &cobra.Command{
		Use:   "rumble",
		Short: "Generate CSV and JSON vulnerability data for display on Academy",
	}

	cmd.PersistentFlags().StringVar(&o.db, "db", "", "BigQuery DB to use")
	cmd.PersistentFlags().StringVar(&o.dbProject, "project", "", "Project hosting the BigQuery DB to query")
	cmd.PersistentFlags().StringVar(&o.storageProject, "gcs-project", "", "GCS project for storage")
	cmd.PersistentFlags().StringVar(&o.storageBucket, "bucket", "", "Bucket in GCS project to save files into")
	cmd.PersistentFlags().BoolVar(&o.upload, "upload", false, "Upload files to GCS bucket")

	cmd.AddCommand(
		cmdVulns(o),
		cmdLegacyCsv(o),
		cmdImageCsvs(o),
	)

	return cmd
}
