FROM cgr.dev/chainguard/nginx:latest@sha256:fdd65ea225da60875e24a8b45d1e65501f9e4991b3b097ae65ed8a4c8f3782a3

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
