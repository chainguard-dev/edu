FROM cgr.dev/chainguard/nginx:latest@sha256:5f1056de9a9fd549e9c2a45476375a886c85c8be2b1545e6ecd1bf8fa78c88aa

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
