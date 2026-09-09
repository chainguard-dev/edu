FROM cgr.dev/chainguard/php:latest-dev@sha256:cb27f34a0c60f5ad825e9dd96599a1d308f5e27dce49c66b3b611f28b0c9cc86

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
