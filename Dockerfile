FROM cgr.dev/chainguard/nginx:latest@sha256:4a7323c4539d04a2d515f7b5f5f449b0d70d06e8128558585c2cabcc05ad2a76

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
