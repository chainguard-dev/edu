FROM cgr.dev/chainguard/php:latest-dev@sha256:f312a03c057542de9fd391eb5927035b263bbc1252da1dece14ade7250214cc6

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
