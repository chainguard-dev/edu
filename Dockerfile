FROM cgr.dev/chainguard/nginx:1

COPY public/ /var/lib/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
