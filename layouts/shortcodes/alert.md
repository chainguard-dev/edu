{{- $context := .Get "context" | default "info" -}}
{{- $body := .Get "text" | default .Inner -}}
> **{{ $context | title }}**: {{ trim $body "\n" | replaceRE "\n" "\n> " }}
