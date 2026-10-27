FROM cgr.dev/chainguard/nginx:latest@sha256:0b4de0f60ae2295fdc852564d178b5473109baf9fc826fa5eb38a59f930e218e

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
