FROM cgr.dev/chainguard/php:latest-dev@sha256:6a5cb6f82c1ccc1ed499ff19bdd15dc6913385d0903eb55356c647489523f68a

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
