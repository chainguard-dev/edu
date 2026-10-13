{{/* Hugo renders a nested {{% tab %}} body to HTML before this template runs, so code here stays HTML. See DOCS-258. */ -}}
**{{ .Get "title" }}**

{{ .Inner }}
