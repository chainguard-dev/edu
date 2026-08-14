/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cmd

import (
	"context"

	"cloud.google.com/go/storage"
)

type GcsClient struct {
	Client *storage.Client
	Ctx    context.Context
	Bucket string
}

func NewGcsClient(ctx context.Context, bucket string) (g GcsClient, err error) {
	g.Ctx = ctx
	g.Client, err = storage.NewClient(ctx)
	if err != nil {
		return GcsClient{}, err
	}

	g.Bucket = bucket
	return g, nil
}

func (g *GcsClient) GetCsvWriter(fName string) (*storage.Writer, error) {
	bkt := g.Client.Bucket(g.Bucket)
	obj := bkt.Object(fName)

	w := obj.NewWriter(g.Ctx)
	w.ContentType = "text/csv"
	w.CacheControl = "public, max-age=60"
	w.ACL = []storage.ACLRule{
		{
			Entity: storage.AllUsers,
			Role:   storage.RoleReader,
		},
	}
	return w, nil
}
