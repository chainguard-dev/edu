FROM cgr.dev/chainguard/nginx:latest@sha256:2d9a58995ee89c05e22ac868ce96057f821090c023be706e415bb77cff9ba41d

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
