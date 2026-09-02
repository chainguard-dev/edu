FROM cgr.dev/chainguard/nginx:latest@sha256:2015f7fa3b514c1bb8de63ed0ebe769295e6d15c5a401fcafbbe555760d42e57

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
