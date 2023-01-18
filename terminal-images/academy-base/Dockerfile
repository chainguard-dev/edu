FROM alpine:3

RUN apk add curl bash tmux sudo tini nano jq && rm -rf /tmp/* /var/cache/apk/*

RUN addgroup inky \
      --gid 1000 && \
    adduser inky \
      --ingroup inky \
      --uid 1000 \
      --system \
      -s /bin/bash
RUN adduser inky wheel

RUN printf "inky:secret" |chpasswd
RUN echo "%wheel ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/wheel

WORKDIR /home/inky
USER inky

ENV COSIGN_EXPERIMENTAL=1
ENTRYPOINT ["/usr/bin/sudo", "/sbin/tini", "--"]
CMD ["/bin/sleep", "3600"]
