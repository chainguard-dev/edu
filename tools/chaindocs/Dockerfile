FROM cgr.dev/chainguard/php:latest-dev@sha256:088c03906d862b8c54dbbe5a32e5c84da48420bcbb2e30ba7be02bd50c0a1c01

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
