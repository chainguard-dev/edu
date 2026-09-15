FROM cgr.dev/chainguard/nginx:latest@sha256:dc9595d10f629d75a1e28e7879d512b48f079d39138b7f3721e9902220c69539

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
