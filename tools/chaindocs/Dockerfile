FROM cgr.dev/chainguard/php:latest-dev@sha256:f084ceb7f0b7aeed6aa54b68c3fc8f222d819827294eb1853dde8e7423679939

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
