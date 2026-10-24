FROM cgr.dev/chainguard/nginx:latest@sha256:cc3cf56e7d34a92db9f4d06bcc839762444b884526764a3ba84421cd8961e86e

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
