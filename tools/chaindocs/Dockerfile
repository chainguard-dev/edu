FROM cgr.dev/chainguard/php:latest-dev@sha256:f06b982330866f6a12bcd43829a2f24eba1e5e41bf9c79e4337eed707fc01eb6

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
