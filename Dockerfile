FROM cgr.dev/chainguard/nginx:latest@sha256:d660885b01f715c21d4bcece4457bef7440cbc8d349b8d5931900cb08b935bdc

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
