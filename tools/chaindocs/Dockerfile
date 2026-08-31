FROM cgr.dev/chainguard/php:latest-dev@sha256:6809b253d4860620834a0b6775492982e38fc459259ddd9e93d3360b31afac02

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
