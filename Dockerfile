FROM cgr.dev/chainguard/nginx:latest@sha256:df0a97604163fb49366d0853c34b238cde40122606f3c92940d47717689a0473

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
