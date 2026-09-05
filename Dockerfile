FROM cgr.dev/chainguard/nginx:latest@sha256:b91cf888522ed0cc1b6bddadfa8320ac2a131a1003b103ae340217a421f12fcc

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
