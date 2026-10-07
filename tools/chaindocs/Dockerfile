FROM cgr.dev/chainguard/php:latest-dev@sha256:e5a19e6582948ce13f7e6f1a22a7272db3b8e7c4ca839d6c083b3c32b190b568

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
