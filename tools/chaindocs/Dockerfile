FROM cgr.dev/chainguard/php:latest-dev@sha256:7df5d4da3ab89b72464cb27662d09901a456788c2cafa02ad07d253b564a624a

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
