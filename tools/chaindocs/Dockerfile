FROM cgr.dev/chainguard/php:latest-dev@sha256:ce76aaeecf13d25ad0e1cfb36f171abac0b7f5baee4e012cb4836836a2e88ab9

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
