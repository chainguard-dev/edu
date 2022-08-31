terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
  required_version = ">= 0.13"

  backend "gcs" {
    bucket = "chainguard-academy-tf-state"
  }
}
