FROM cgr.dev/chainguard/nginx:latest@sha256:aa1ad3cd86d52b85d86edb8d73b1d00698b74958af5928e5cae3b786f4263afb

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
