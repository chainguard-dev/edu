/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"encoding/json"
	"os"
)

func (r *results) marshal() error {
	for _, l := range unchecked.Links {
		l.FullURL = l.URL.String()
		r.Unchecked = append(r.Unchecked, l)
	}

	for _, l := range checked.Links {
		l.FullURL = l.URL.String()
		r.Checked = append(r.Checked, l)
	}

	for _, l := range ignored.Links {
		l.FullURL = l.URL.String()
		r.Ignored = append(r.Ignored, l)
	}

	var err error
	if r.json, err = json.MarshalIndent(r, "", "  "); err != nil {
		return err
	}

	return nil
}

func (r *results) write() error {
	return os.WriteFile(resultsFile, r.json, os.ModePerm)
}
