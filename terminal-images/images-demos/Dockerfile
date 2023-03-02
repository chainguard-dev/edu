FROM academy-base:latest

RUN sudo apk add git docker && sudo rm -rf /tmp/* /var/cache/apk/*
RUN sudo adduser inky docker
RUN git clone https://github.com/chainguard-dev/edu-images-demos.git

WORKDIR /home/inky/edu-images-demos
 
CMD ["/usr/bin/dockerd"]
