FROM cgr.dev/chainguard/php:latest-dev@sha256:9dccb6c2ac97179fa968767b9e7711240cb3480807ba02080a6ad66446fd0935

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
