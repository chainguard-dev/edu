variable "project_id" {
  description = "The project ID where all resources created will reside."
  type        = string
}

variable "name" {
  description = "Name indicator, prefixed to resources created."
  type        = string
}

variable "primary-region" {
  description = "The region where this environment's databases and batch processes should run."
  type        = string
}

variable "image" {
  description = "The container image to deploy."
  type        = string
}
