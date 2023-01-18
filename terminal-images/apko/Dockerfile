FROM academy-base:latest

RUN sudo apk add docker && rm -rf /tmp/* /var/cache/apk/*
RUN sudo adduser inky docker

CMD ["/usr/bin/dockerd"]
