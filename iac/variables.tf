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

variable "mcp_image" {
  description = "The container image for the MCP HTTP server. Managed by CI after initial creation."
  type        = string
  default     = "ghcr.io/chainguard-dev/ai-docs:latest"
}
