FROM cgr.dev/chainguard/nginx:latest@sha256:f6cbe96998972d87ebe30952ec1b6f3cff4103c33c889ffca7e13053e2036571

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
