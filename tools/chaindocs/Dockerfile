FROM cgr.dev/chainguard/php:latest-dev@sha256:6049f1657453c03145d6230fec72c342ae62d6a6003f943d31d0308f68e7b8bb

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
