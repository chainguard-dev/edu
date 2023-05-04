FROM cgr.dev/chainguard/nginx:latest

COPY public/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
