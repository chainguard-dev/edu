FROM cgr.dev/chainguard/php:latest-dev@sha256:c5e989c5cedca3b979e8172939dac16926d731a91d83d3d5b4203bc6d8ef0079

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
