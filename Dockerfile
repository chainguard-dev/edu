FROM cgr.dev/chainguard/nginx:latest@sha256:65ad444a372b9f69821ef15acb95c46e9cffdd520bbdc4f8a72d5d38d7c1ca92

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
