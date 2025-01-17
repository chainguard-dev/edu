FROM cgr.dev/chainguard/nginx:latest

COPY public/ /usr/share/nginx/html/
COPY redirects /etc/nginx/redirects
COPY nginx.conf /etc/nginx/nginx.conf
