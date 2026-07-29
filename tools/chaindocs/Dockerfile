FROM cgr.dev/chainguard/php:latest-dev@sha256:aa87e4d66017b9f3c24da1ca726325caa0cd973523819f48dc94440d6f2be208

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
