FROM cgr.dev/chainguard/php:latest-dev@sha256:9f5082b198fe5a0e6dce2cce645a327cdc1049fa82020ac4876279c031d6dc74

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
