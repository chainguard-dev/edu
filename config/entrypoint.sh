#!/bin/bash

su - inky -s /bin/bash -c '/usr/sbin/nginx -c /etc/nginx/nginx.conf -e /dev/stderr -g "daemon on;" > /dev/null 2>&1'
printf "\nWelcome to the Academy development environment!\n\n"
export PS1="[academy] ❯ "
export GOPATH="/root/.cache/go"
export CGO_ENABLED=0
bash -i
