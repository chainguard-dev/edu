FROM cgr.dev/chainguard/php:latest-dev@sha256:f4874e551bc9ceb23a244ba0ff4092b43cd1363abea3714797f7efab07648247

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
