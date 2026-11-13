FROM cgr.dev/chainguard/nginx:latest@sha256:a2bbeeda97bb059018d7a022b3d704e2c0ac55ca738e6f7654ae743189dac24e

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
