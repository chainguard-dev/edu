FROM cgr.dev/chainguard/php:latest-dev@sha256:6463a4b6285d96ec01b489439c5b7f36707d9d3e28a99f7febc90cc78247f0d8

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
