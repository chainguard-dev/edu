FROM cgr.dev/chainguard/nginx:latest@sha256:c5b581989f162fca74cfdc54d7e868545599605b47873dfacffcbc247d8b6637

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
