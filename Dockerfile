FROM cgr.dev/chainguard/nginx:latest@sha256:d166cfff80ac94040ccc52c6a42768486483514f7494ca641a68399655b4a053

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
