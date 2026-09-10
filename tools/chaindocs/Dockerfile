FROM cgr.dev/chainguard/php:latest-dev@sha256:528d980dec0f9d9d74499ecfb00f84982130aee9167a78b7ec37db7826b34659

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
