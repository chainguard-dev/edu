FROM cgr.dev/chainguard/php:latest-dev@sha256:5d240a1d22d88b11d7eac0bfaa96fc693c5e3c1fc792daa7ff078a4a60f8662c

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
