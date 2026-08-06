FROM cgr.dev/chainguard/nginx:latest@sha256:171bc52d7bb01604bfb107800e646a02915ec9f98fb145659bb859955d1d7f51

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
