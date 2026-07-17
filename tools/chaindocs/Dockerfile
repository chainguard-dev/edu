FROM cgr.dev/chainguard/php:latest-dev@sha256:c29e0cd3116eb08cb90a85e0ff3f774774a1918e63d77560d9c37c00c0576f1c

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
