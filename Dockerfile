FROM cgr.dev/chainguard/nginx:latest@sha256:2189489ef3fa5b1e94a8463f98f9c148a4d8e7498d3f747069fc78de405742fc

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
