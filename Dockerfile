FROM cgr.dev/chainguard/nginx:latest@sha256:a0ddb6f13562105c6a0b473d0e9ff8a6e2bf8aa3d2e17c08d170b2fef0f2a0e6

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
