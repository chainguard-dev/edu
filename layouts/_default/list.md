# {{ .Title }}

URL: {{ .Permalink | replaceRE "/$" ".md" }}
{{- if .Description }}

{{ .Description }}
{{- end }}

## Pages

{{ range .RegularPages -}}
- [{{ .Title }}]({{ .Permalink | replaceRE "/$" ".md" }}){{ with .Description }}: {{ . }}{{ end }}
{{ end }}
