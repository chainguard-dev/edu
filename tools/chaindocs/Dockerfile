FROM cgr.dev/chainguard/php:latest-dev@sha256:744f1bababffa61faf9db17c0529f74b091cd1f446cff5f028b8902b5eec10e9

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
