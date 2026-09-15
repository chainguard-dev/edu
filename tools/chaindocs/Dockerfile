FROM cgr.dev/chainguard/php:latest-dev@sha256:f1d65c5399d060586e6891d74313878cdfa9a30e75f182aae17276dee9caca27

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
