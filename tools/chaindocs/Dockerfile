FROM cgr.dev/chainguard/php:latest-dev@sha256:937f6af540198c9080e19abb2c6afa99bfc466cfa330321cd32366356124f941

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
