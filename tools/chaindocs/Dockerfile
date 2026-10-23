FROM cgr.dev/chainguard/php:latest-dev@sha256:d6c8da50ebe631f3c77fe9f36d04064bb0d20750efbc2452d435918c566aefaa

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
