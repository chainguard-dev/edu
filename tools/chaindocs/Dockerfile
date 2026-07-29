FROM cgr.dev/chainguard/php:latest-dev@sha256:f30adc06d58488f44ae84e91262355e8c02c3abdfa814f81264b8771771b86ef

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
