{{- /*
  Permission note for `chainctl libraries update-hashes`.
  Usage: {{% blurb/libraries-update-hashes-permissions ecosystem="python" %}}
*/ -}}
{{- $ecosystem := .Get "ecosystem" -}}
> **Note**: With a regular `chainctl auth login`, `chainctl libraries update-hashes` creates a pull token, which requires the `libraries.{{ $ecosystem }}.pull_token_creator` role or the `owner` role. With only the `libraries.{{ $ecosystem }}.pull` role, sign in with `chainctl auth login --audience=libraries.cgr.dev` or pass a libraries-scoped token. For details, refer to [Authentication](/chainguard/libraries/{{ $ecosystem }}/build-configuration/#update-hashes-auth).
