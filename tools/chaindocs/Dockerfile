FROM cgr.dev/chainguard/php:latest-dev@sha256:c5468691e5fcd62fc743b853edf3aaabc04c92889fed926853c8c2f3b30eb016

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
