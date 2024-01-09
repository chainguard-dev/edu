terraform {
  backend "gcs" {
    bucket = "chainguard-academy-terraform-state"
    prefix = "/ng-academy"
  }
}

provider "google" { project = var.project_id }
provider "google-beta" { project = var.project_id }

module "networking" {
  source  = "chainguard-dev/common/infra//modules/networking"
  version = "0.2.0"

  name       = var.name
  project_id = var.project_id
  regions    = [var.primary-region]
}

resource "google_service_account" "chainguard-academy" {
  project = var.project_id

  account_id   = var.name
  display_name = "Chainguard Academy"
  description  = "The unprivileged service account as which Chainguard academy runs."
}

resource "google_cloud_run_v2_service" "chainguard-academy" {
  for_each = module.networking.regional-networks

  project  = var.project_id
  name     = var.name
  location = each.key
  ingress  = "INGRESS_TRAFFIC_ALL"

  launch_stage = "BETA" // Needed for vpc_access below

  template {
    vpc_access {
      network_interfaces {
        network    = each.value.network
        subnetwork = each.value.subnet
      }
      // Academy does not egress
      egress = "ALL_TRAFFIC"
    }

    service_account = google_service_account.chainguard-academy.email
    containers {
      image = var.image

      ports {
        container_port = 8080
      }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public-services-are-unauthenticated" {
  for_each = google_cloud_run_v2_service.chainguard-academy

  project  = var.project_id
  location = each.key
  name     = each.value.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

output "urls" {
  value = { for k, v in google_cloud_run_v2_service.chainguard-academy : k => v.uri }
}
