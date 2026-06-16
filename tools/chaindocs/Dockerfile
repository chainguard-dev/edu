FROM cgr.dev/chainguard/php:latest-dev@sha256:baee2b6a52306844028b3e54f8afedeba24246c7b3fc820389985895b7740a70

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
