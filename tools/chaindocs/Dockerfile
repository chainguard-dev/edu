FROM cgr.dev/chainguard/php:latest-dev@sha256:42838e02dd49cbe6402f1a738b4730452791cdfa7f6898697da81098dd01fd46

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
