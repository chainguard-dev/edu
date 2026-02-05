FROM cgr.dev/chainguard/nginx:latest@sha256:17f2bec74555f5602eb6c562a8587800d1e31c379082e6123adac08fe41c037a

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
