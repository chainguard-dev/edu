FROM cgr.dev/chainguard/php:latest-dev@sha256:c9e4a84eff3a3b142a02446f44d4a216ddbc402df64a7f39a682d32e041d7674

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
