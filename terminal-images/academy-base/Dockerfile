FROM alpine:3

RUN apk add curl bash bash-completion tmux sudo tini nano jq && rm -rf /tmp/* /var/cache/apk/*

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

ENTRYPOINT ["/usr/bin/sudo", "/sbin/tini", "--"]
CMD ["/bin/sleep", "3600"]
