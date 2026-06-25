FROM cgr.dev/chainguard/php:latest-dev@sha256:802af43e359517462ce01d77990a43321f9d132e5d07c151d1dda05ebc085a93

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
