FROM cgr.dev/chainguard/nginx:latest@sha256:cd35918ef80082318a9215becdb351c964435193003f281ebb8d5de872562ccd

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
