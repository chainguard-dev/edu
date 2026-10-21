FROM cgr.dev/chainguard/nginx:latest@sha256:8a42fb9468e353a6c2501d2657866333b7a2a075912f4a7e4fa73298aafd46d6

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
