FROM cgr.dev/chainguard/php:latest-dev@sha256:dffc998ac0f03c5ee1c1b82e8adb28d09ef293b68a91930aa7d7a9b605ef84c4

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
