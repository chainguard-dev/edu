FROM cgr.dev/chainguard/nginx:latest@sha256:c85033c0053e4b65bca6f7cc4770c437f4860cc688e227c769ca6e48daf2e308

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
