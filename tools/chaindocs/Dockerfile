FROM cgr.dev/chainguard/php:latest-dev@sha256:c8fb2e72b0f62c93c67d399968fd3214c68c6a7f10390c7205e4d45b46b9088b

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
