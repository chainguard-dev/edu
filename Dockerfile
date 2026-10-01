FROM cgr.dev/chainguard/nginx:latest@sha256:a57e76e6fc57826717c7696df82441f66a835205b3f09232a598840e2fac7786

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
