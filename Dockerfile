FROM cgr.dev/chainguard/nginx:latest@sha256:b9debc2fbe5bf256b4c3980d0bbfda8187d46e35b4117c582ace66269dc1de28

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
