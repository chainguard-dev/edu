FROM cgr.dev/chainguard/nginx:latest@sha256:cfd045c63b7ff6c038f8039e8d2ac09b4c40213ff1505a6834852c6460ec8d2d

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
