FROM academy-base:latest

USER root
RUN apk add supervisor && rm -rf /tmp/* /var/cache/apk/*

COPY supervisord.conf /etc/supervisord.conf
RUN printf 'alias kubectl="k3s kubectl"\nalias k="k3s kubectl"\nsource <(kubectl completion bash)\ncomplete -o default -F __start_kubectl k\n' >> /etc/bash/bashrc
RUN mkdir -p /var/log/ /var/lib/rancher/k3s/server/manifests
RUN wget https://github.com/k3s-io/k3s/releases/download/v1.26.1%2Bk3s1/k3s && mv k3s /usr/local/bin/ && chmod +x /usr/local/bin/k3s
COPY policy-controller.yaml /var/lib/rancher/k3s/server/manifests

USER inky
ENTRYPOINT ["/usr/bin/sudo", "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
