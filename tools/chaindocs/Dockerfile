FROM cgr.dev/chainguard/php:latest-dev@sha256:a78927bb23648856013b76471efc665c9b385b494e071bc83f7270e14696655f

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
