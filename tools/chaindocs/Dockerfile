FROM cgr.dev/chainguard/php:latest-dev@sha256:08d24892b614ddf8e81868ce42caf7562d4791eefd368a736888b0b807bc9b07

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
