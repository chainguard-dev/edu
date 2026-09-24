FROM cgr.dev/chainguard/php:latest-dev@sha256:47fb4c876bef96187e61f2ef128b5e2ab4a1c9162fc97cd9a23f3bd5a9f008a6

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
