FROM cgr.dev/chainguard/php:latest-dev@sha256:a99a684523e6032a1f8cceb89bf338550df948b151425f545dec87eeff129423

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
