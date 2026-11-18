FROM cgr.dev/chainguard/php:latest-dev@sha256:0ce245030db1935938b0790d0800e9ac3aff6c94f2649225561c96dd90e6011a

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
