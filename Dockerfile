FROM cgr.dev/chainguard/nginx:latest@sha256:d74ba9e5cf9f6b049807e27a5a14a8cd2550ac428143b7d15ea3dbad282f4ed1

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
