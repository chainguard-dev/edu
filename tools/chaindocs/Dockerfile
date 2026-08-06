FROM cgr.dev/chainguard/php:latest-dev@sha256:9bcf1f2341442fef2c124f29ddfe78a0e928a6f9f31018c9560374dc706ed15e

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
