FROM cgr.dev/chainguard/nginx:latest@sha256:0352063c168740414d8caf7cbcc2b386506dba82ba3955cfaee2b8582a1a93a8

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
