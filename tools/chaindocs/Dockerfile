FROM cgr.dev/chainguard/php:latest-dev@sha256:872ee3e20eeae4db87c12c1e8af0288dcff1bde5fce725adc5ba9c6b3a98d503

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
