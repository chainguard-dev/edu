{{- $feature := .Get "feature" | default "This feature" -}}
> **Note**: {{ $feature }} is in beta.
{{- if eq (.Get "enroll") "true" }} Contact your Chainguard account team to enable it for your organization.{{ end -}}
{{- with .Get "access" }} Available to {{ . }}.{{ end -}}
{{- if eq (.Get "feedback") "true" }} Share feedback with your account team.{{ end }}
