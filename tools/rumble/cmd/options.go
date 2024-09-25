/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cmd

import (
	"context"
	"log"

	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	cloudstorage "github.com/chainguard-dev/edu/tools/rumble/pkg/cloudstorage"
)

type rumbleBase struct {
	ctx           context.Context
	bqClient      cgbigquery.BqClient
	storageClient cloudstorage.GcsClient
	opts          *options
}

type options struct {
	dbProject      string
	storageProject string
	db             string
	storageBucket  string
	upload         bool
}

func (c *rumbleBase) setupClients() (func(), error) {
	var err error

	c.bqClient, err = cgbigquery.NewBqClient(c.opts.dbProject, c.opts.db)
	if err != nil {
		log.Fatalf("error initializing bq client: %v", err)
	}

	// Only instantiate gcs client if we're uploading
	if c.opts.upload {
		c.storageClient, err = cloudstorage.NewGcsClient(c.ctx, c.opts.storageBucket)
		if err != nil {
			log.Fatalf("error initializing gcs client: %v", err)
		}
	}

	return func() {
		if err := c.bqClient.Client.Close(); err != nil {
			log.Println(err)
		}
		if c.storageClient.Client != nil {
			if err := c.storageClient.Client.Close(); err != nil {
				log.Println(err)
			}
		}
	}, nil
}
