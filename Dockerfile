FROM cgr.dev/chainguard/nginx:latest@sha256:c516cddebbf0613c8020a9bd9b44e54a9feafc9742a1f1a04cb8d08bf55ef212

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
