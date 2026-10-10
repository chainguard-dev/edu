FROM cgr.dev/chainguard/nginx:latest@sha256:f77f61de0f1001a54f3186e8a62adcde80c946603b88379263cf6f3bbaab54a7

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
