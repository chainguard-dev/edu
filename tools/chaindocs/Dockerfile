FROM cgr.dev/chainguard/php:latest-dev@sha256:39f4cbf55bc2368a21972ddf0405b5f41dab7e14d4d37238e744320db1b39722

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
