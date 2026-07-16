FROM cgr.dev/chainguard/php:latest-dev@sha256:2aee15785000e38d45592baf6f53e12ca126028a3e035e1d398f9040a02ff451

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
