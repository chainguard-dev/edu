FROM cgr.dev/chainguard/php:latest-dev@sha256:316f8dc2f767c24103167286546c53108dd5c2717326d39d4e6eb80a9e96fc3d

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
