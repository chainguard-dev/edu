FROM cgr.dev/chainguard/nginx:latest@sha256:4ba9811960f4a9c987a9cea0d445fbff98bd28164d5f7ccc465558d1b7225213

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
