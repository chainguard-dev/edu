FROM cgr.dev/chainguard/nginx:latest@sha256:9d34c0a9f349eaf64ec75b3e8c09774fa234152a03cee94121e09e7220e2a560

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
