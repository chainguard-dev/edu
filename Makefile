cfg?=apko.yaml
arch := $(shell uname -m)

.PHONY: apko-build dev-container
apko-build:
	docker run --rm -v $$PWD:/work -it cgr.dev/chainguard/apko:latest build \
	--repository-append https://packages.wolfi.dev/os \
	--keyring-append    https://packages.wolfi.dev/os/wolfi-signing.rsa.pub \
	--package-append    wolfi-baselayout \
	--arch              $(arch) \
	/work/$(cfg) academy.local /work/academy.tar
	docker load < academy.tar
	rm academy.tar

dev-container:
	docker run --rm \
	-v $$PWD/config/entrypoint.sh:/entrypoint.sh \
	-v $$PWD/public:/usr/share/nginx/html \
	-v $$PWD/nginx.conf:/etc/nginx/nginx.conf \
	-v $$PWD:/home/inky/ \
	-p 8080:8080 -p 1313:1313 \
	-it --user root \
	apko.local:latest-$(arch)
