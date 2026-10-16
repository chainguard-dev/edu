FROM cgr.dev/chainguard/nginx:latest@sha256:bbed24ea6459404aeaf23edca30844092adee4d6059808cda5ebf9456a43d874

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
