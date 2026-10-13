FROM cgr.dev/chainguard/php:latest-dev@sha256:ecddcc815f03f2d084520a9615a9356e7cd5a8662665ae0cc2a2bc1c02e272bb

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
