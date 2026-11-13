{{- /*
  Permission note for `chainctl libraries verify`.
  Usage: {{% blurb/libraries-verify-permissions ecosystem="java" %}}
  Omit `ecosystem` on pages that cover every ecosystem.
*/ -}}
{{- $ecosystem := .Get "ecosystem" -}}
{{- if $ecosystem -}}
> **Note**: With a regular `chainctl auth login`, running `chainctl libraries verify` requires the `libraries.{{ $ecosystem }}.pull_token_creator` role or the `owner` role, because the command creates a pull token. With only the `libraries.{{ $ecosystem }}.pull` role, pass a libraries-scoped token instead, as described in [Verify with a pull role](/chainguard/libraries/policies-and-security/verification/#verify-with-a-pull-role).
{{- else -}}
> **Note**: With a regular `chainctl auth login`, running `chainctl libraries verify` requires the `pull_token_creator` role for the ecosystem you verify, such as `libraries.java.pull_token_creator`, or the `owner` role, because the command creates a pull token. With only a `pull` role, pass a libraries-scoped token instead, as described in [Verify with a pull role](/chainguard/libraries/policies-and-security/verification/#verify-with-a-pull-role).
{{- end -}}
