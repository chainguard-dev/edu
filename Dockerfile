FROM cgr.dev/chainguard/nginx:latest@sha256:4d1a034e20cf62edc65b279e83025deec3dfb38bee92cde9e5d51b44752fd7f9

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
