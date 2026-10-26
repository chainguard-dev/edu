FROM cgr.dev/chainguard/nginx:latest@sha256:9aa6c46648f17b2835d009fd4338b38591b2396670a07270ee19b532f83dbbb5

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
