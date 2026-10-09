FROM cgr.dev/chainguard/php:latest-dev@sha256:c4323620812f425d931473800f65d238d67d955c4c839717f9a14ee0ccc88c85

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
