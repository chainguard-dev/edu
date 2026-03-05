FROM cgr.dev/chainguard/php:latest-dev@sha256:39dbdf63db1cc978a8e06d99d246ca57ee0f882cdf571655b6e1c517c9a81f7d

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
