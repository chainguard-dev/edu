FROM cgr.dev/chainguard/php:latest-dev@sha256:a6f88f32db9d3eaa9ff5aa8c2dfca2795b10c2c57d17811ecfbb149df2bc3102

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
