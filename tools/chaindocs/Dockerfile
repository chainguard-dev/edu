FROM cgr.dev/chainguard/php:latest-dev@sha256:f1eaeeddcaf6ef0bd7856690b689ce1a865fc13e21dc5827ba8376d0baf3aeff

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
