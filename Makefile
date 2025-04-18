cfg?=apko.yaml
arch := $(shell uname -m)

.PHONY: apko-build dev-container chaindocs
apko-build:
	docker run --rm -v $$PWD:/work -it cgr.dev/chainguard/apko:latest build \
	--arch              $(arch) \
	/work/$(cfg) academy.local /work/academy.tar
	docker load < academy.tar
	rm academy.tar

dev-container:
ifeq ("$(arch)","x86_64")
	docker run --rm \
	-v $$PWD/config/entrypoint.sh:/entrypoint.sh \
	-v $$PWD/public:/usr/share/nginx/html \
	-v $$PWD/nginx.conf:/etc/nginx/nginx.conf \
	-v $$PWD:/home/inky/ \
	-p 8080:8080 -p 1313:1313 \
	-it --user root \
	academy.local:latest-amd64
else
	docker run --rm \
	-v $$PWD/config/entrypoint.sh:/entrypoint.sh \
	-v $$PWD/public:/usr/share/nginx/html \
	-v $$PWD/nginx.conf:/etc/nginx/nginx.conf \
	-v $$PWD:/home/inky/ \
	-p 8080:8080 -p 1313:1313 \
	-it --user root \
	academy.local:latest-$(arch)
endif

chaindocs:
	@echo "Building Chaindocs..."
	docker  build tools/chaindocs -t chaindocs.local
	@echo "Running Chaindocs..."
	docker run --rm \
	-v $$PWD/content:/app/content \
	-e CONTENT_DIR=/app/content \
	-it --entrypoint /bin/sh \
	chaindocs.local
