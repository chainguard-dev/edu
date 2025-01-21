FROM cgr.dev/chainguard/nginx:latest

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf

RUN ["/usr/sbin/nginx", "-t"] || (echo "❌ Nginx configuration test failed. Check aliases in front matter or any updates to nginx.conf" && exit 1)
