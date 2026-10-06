FROM cgr.dev/chainguard/php:latest-dev@sha256:a07ecb32b384f6578284b062b0a1651e7ae41a8e57d32ea40ab8d061266b8323

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
