FROM cgr.dev/chainguard/php:latest-dev@sha256:fe4da1b5e5c17959ec6d904681e3e98cafd54e5ee3b0d110e3871b9ea8673e39

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
