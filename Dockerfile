FROM cgr.dev/chainguard/nginx:latest@sha256:76cc70e5e8da88ae76ff585525c340fc09d54018c5c902551d61a24c2b3ac0d2

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
