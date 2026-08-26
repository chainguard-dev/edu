FROM cgr.dev/chainguard/nginx:latest@sha256:fe96e6c379821c0461f006a5545a872d9c3ea1942d5c46623d40bfa37c829c33

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
