FROM cgr.dev/chainguard/php:latest-dev@sha256:f8a3b72b9df8b5ac5d710f9cd9991a6353bbc1a2bf56e3a75467ab422a34579e

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
