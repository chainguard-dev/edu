FROM cgr.dev/chainguard/nginx:1

COPY public/ /var/lib/nginx/html/
COPY htpasswd /etc/nginx/.htpasswd
COPY nginx.conf /etc/nginx/nginx.conf
