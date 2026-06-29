FROM cgr.dev/chainguard/php:latest-dev@sha256:c391e2cbe76d041c3481489b79ee311bdb45bf0b625f58b862467a0fbf9f6469

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
