FROM cgr.dev/chainguard/php:latest-dev

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

ENTRYPOINT [ "php", "/app/chaindocs" ]
