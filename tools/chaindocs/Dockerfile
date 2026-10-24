FROM cgr.dev/chainguard/php:latest-dev@sha256:7e28c85e231476d1f5c6290061ef57b9acccc34dc8e19ecea437f10787e5712c

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
