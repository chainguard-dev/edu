resource "google_project" "chainguard-academy" {
  name = var.project_id
  project_id = var.project_id
  folder_id = 688879595725
  billing_account = var.billing_account
}

resource "google_app_engine_application" "chainguard-academy" {
  project = var.project_id
  location_id = "us-central"
}

resource "google_project_service" "cloudbuild" {
  project = var.project_id
  service = "cloudbuild.googleapis.com"
}

resource "google_project_service" "iap" {
  project = var.project_id
  service = "iap.googleapis.com"
}

resource "google_iap_web_iam_binding" "binding" {
  project = var.project_id
  role = "roles/iap.httpsResourceAccessor"
  members = [
    "domain:chainguard.dev",
  ]
}

resource "google_iap_brand" "project_brand" {
  support_email     = "jamon@chainguard.dev"
  application_title = "Chainguard Academy"
}
