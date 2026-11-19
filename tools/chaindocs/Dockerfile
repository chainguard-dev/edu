FROM cgr.dev/chainguard/php:latest-dev@sha256:e108461fb670d0a439ffb6fd95d1ed84478621e8e0e477fc7289d5a5dcfe2034

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
