FROM cgr.dev/chainguard/php:latest-dev@sha256:9461a5467841b58ef305184377bd568e65530a9fa3d02976d9ff0c982b7f9002

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
