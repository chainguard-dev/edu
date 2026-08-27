FROM cgr.dev/chainguard/php:latest-dev@sha256:ba023c31154ddfa17680b068ebcf5e06c536169232d293a4a523717879bb64e4

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
