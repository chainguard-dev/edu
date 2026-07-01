FROM cgr.dev/chainguard/php:latest-dev@sha256:f36270ba7a90f2a91a9270da40e2bd71728727c7d08dffe1bc209d1b3f1a461d

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
