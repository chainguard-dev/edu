FROM cgr.dev/chainguard/nginx:latest@sha256:919245025f299eba38530d49a63f3799e4bbdf6c06106490c399710c4ba55023

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
