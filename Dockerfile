FROM cgr.dev/chainguard/nginx:latest@sha256:7e12e9b01337d6f0039a0dbf41d97e3abf26fe62c0c9e94c9969bad2398b0973

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
