FROM cgr.dev/chainguard/php:latest-dev@sha256:9450910150eb62fb110b5495eee2a0eb6629ca45f6f1138a458481054a128c78

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
