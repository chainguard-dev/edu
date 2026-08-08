FROM cgr.dev/chainguard/php:latest-dev@sha256:4079e334ea9a8c497d172980cb651c1046e76ad77becd5db3cdc18146ea84993

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
