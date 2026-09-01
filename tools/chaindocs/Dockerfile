FROM cgr.dev/chainguard/php:latest-dev@sha256:81feeaec8858de10b8078d7e9f911bb0d01eed83241184e4a095a0bc87a241ff

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
