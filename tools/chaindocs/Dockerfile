FROM cgr.dev/chainguard/php:latest-dev@sha256:72a62ad4cef3fc7754f18bbf028f6499a92fef3e055d33ae732fa09fad821db4

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
