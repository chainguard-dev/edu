FROM cgr.dev/chainguard/nginx:latest@sha256:1d942360cecf98fe7e45c0470b23734b3c62868544380f920d1c1fa9de6e8e27

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
