package main

import (
	"os"
	"testing"
)

func TestWalkDir(t *testing.T) {
	validDir, err := os.MkdirTemp("", "validDir")
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll(validDir)

	tests := []struct {
		name    string
		dir     string
		wantErr bool
	}{
		{"Valid contentDir", validDir, false},
		{"Nonexistent contentDir", "invalidDir", true},
		{"Invalid contentDir", "really,an,invalidDir", true},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			contentDir = tc.dir // override the global runtime flag
			err := processContentDir()
			switch tc.wantErr {
			case true:
				if err == nil {
					t.Errorf("expected an error for directory %s, but got none", tc.dir)
				}
			case false:
				if err != nil {
					t.Errorf("unexpected error for directory %s: %v", tc.dir, err)
				}
			}
		})
	}
}
