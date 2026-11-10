FROM cgr.dev/chainguard/php:latest-dev@sha256:3d01649638f33f261b5c195b405fb216f00e79a5c1845f565205350bb0f2eafd

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
