FROM academy-base:latest

RUN sudo apk add docker cosign && rm -rf /tmp/* /var/cache/apk/*
RUN sudo adduser inky docker

CMD ["/usr/bin/dockerd"]
