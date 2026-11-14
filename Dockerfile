FROM cgr.dev/chainguard/nginx:latest@sha256:3efdf56b9730d56a9bc88edf268ab72ee965cbb7d116291a8679cd89ef67e0c5

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
