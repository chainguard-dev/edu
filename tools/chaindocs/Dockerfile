FROM cgr.dev/chainguard/php:latest-dev@sha256:7cd217f4a8bcfc9d8f455f6c441e00f4a318bede82cb0a7b2f10649df9aa7fbf

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
