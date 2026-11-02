FROM cgr.dev/chainguard/php:latest-dev@sha256:1f7c2e214a55288b1722026801e1157123b99aa62187674c40380d04e3375e01

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
