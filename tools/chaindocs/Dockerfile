FROM cgr.dev/chainguard/php:latest-dev@sha256:6fa3228af99fe74328896ecfbc2f5123a7003630468f7fb49bad1531ebf68a17

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
