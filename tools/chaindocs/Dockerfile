FROM cgr.dev/chainguard/php:latest-dev@sha256:9192f233a408ac443e1141410552684c1c76b7b7c0e2e53b46a6873ba5604361

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
