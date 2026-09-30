FROM cgr.dev/chainguard/nginx:latest@sha256:98b92f87f0ceb43d45a63db62df6e7b6ec6e2efe1bcf09975a2af1ed7edfc438

COPY public/ /usr/share/nginx/html/
COPY public/_aliases /etc/nginx/aliases
COPY nginx.conf /etc/nginx/nginx.conf
