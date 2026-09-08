FROM cgr.dev/chainguard/php:latest-dev@sha256:19e3db9c392993513210b5b77f44903df69656794a0f8e29502cb8b8cd8199a3

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
