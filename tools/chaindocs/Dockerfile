FROM cgr.dev/chainguard/php:latest-dev@sha256:003c54f205d399420c382254660e0c6bb9e460b69dbb3bb0d298cf0c1a4b87a0

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
