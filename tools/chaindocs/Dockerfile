FROM cgr.dev/chainguard/php:latest-dev@sha256:c81fa48a2bd8464caf7b06e3b09c3519a121ec0f4ecca04431a7c571771f7cb1

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
