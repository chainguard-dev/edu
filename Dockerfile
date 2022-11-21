FROM cgr.dev/chainguard/nginx:latest

COPY public/ /var/lib/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
