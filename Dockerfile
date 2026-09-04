FROM cgr.dev/chainguard/nginx:latest@sha256:8a4981bd9d32dcf4406bbbac259565962f15c5c3cc235bf9df98fe2e5a9cea19

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
