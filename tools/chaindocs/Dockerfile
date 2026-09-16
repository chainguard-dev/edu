FROM cgr.dev/chainguard/php:latest-dev@sha256:bdb449a859c0cd630a87735723ec0e46defbdf47024701f551fb708fa6731fae

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
