FROM cgr.dev/chainguard/php:latest-dev@sha256:e9388002499f0e8f07d77a603e35b28fe255853f283dc38e2e9b61275a8104ca

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
