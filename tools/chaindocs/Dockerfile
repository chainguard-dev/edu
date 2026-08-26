FROM cgr.dev/chainguard/php:latest-dev@sha256:5ee6afea277e458bf2eda5bbe01574e61c0af6f2029dc6f7364accd112234c6a

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
