FROM cgr.dev/chainguard/php:latest-dev@sha256:4a6b2c4bd10676f58f58c905acd7a5e624db45310efe13706d326637a1dbf819

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
