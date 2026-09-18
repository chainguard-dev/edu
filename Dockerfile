FROM cgr.dev/chainguard/nginx:latest@sha256:d770a59f02e443a1403d44f4d6c0eb74b076a2433f3df9e0f4782fe4bff2ac22

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
