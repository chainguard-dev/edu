FROM cgr.dev/chainguard/php:latest-dev@sha256:1fc64c7aa2d8821eec84021b5d7d0bb8ffc999b5a6cd401bf7e79a92011d464c

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
