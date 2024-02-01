/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import "github.com/chainguard-dev/edu/tools/rumble/cmd"

func main() {
	err := cmd.New().Execute()
	if err != nil {
		panic(err)
	}
}
