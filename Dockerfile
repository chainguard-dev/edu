FROM cgr.dev/chainguard/nginx:latest@sha256:5b397d323878cd75f6c6968b2836bf5497b6e2d29f0cd7609f8d9d03ea6db2e6

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
