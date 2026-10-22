FROM cgr.dev/chainguard/php:latest-dev@sha256:878a35e95f99b2f12a50f4e7f09b0136c9c300420e8e7dfefdc2db2ccd040978

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
