FROM cgr.dev/chainguard/nginx:latest@sha256:a0a6cc87a5a02b27ac0bf10b7a108ff825e8cb832f25952bbc04c69605a98b35

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
