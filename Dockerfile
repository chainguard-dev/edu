FROM cgr.dev/chainguard/nginx:latest@sha256:c3e810caa72b130c880f750986c2bab5ea7ca7ad03365ea562718be77d7d7c2e

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
