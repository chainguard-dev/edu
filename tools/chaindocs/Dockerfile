FROM cgr.dev/chainguard/php:latest-dev@sha256:6de8e0eef8914954414020ebddcc1bab52f3e1bb88555262cce4b6020b38d87a

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
