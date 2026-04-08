# {{ .Title }}

URL: {{ .Permalink | replaceRE "/$" ".md" }}
Last Modified: {{ .Lastmod.Format "January 2, 2006" }}
{{- if .Params.tags }}
Tags: {{ delimit .Params.tags ", " }}
{{- end }}
{{- if .Description }}

{{ .Description }}
{{- end }}

{{ .Content | plainify }}
