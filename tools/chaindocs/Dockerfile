FROM cgr.dev/chainguard/php:latest-dev@sha256:f4971a7fe28c12ee333c737e37892c8eb71ca657a112bada70530f5f3c8ae108

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
