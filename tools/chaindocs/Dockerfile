FROM cgr.dev/chainguard/php:latest-dev@sha256:774042ccab5b7cba78748dcafa9c9090c0a37802670615de7dcd7614554f77e4

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
