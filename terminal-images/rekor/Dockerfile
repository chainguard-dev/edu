FROM --platform=linux/amd64 golang:1.19 as builder

RUN GOOS=linux CGO_ENABLED=0 GOARCH=amd64 go install -v github.com/sigstore/rekor/cmd/rekor-cli@latest

FROM --platform=linux/amd64 academy-base:latest

COPY --from=builder /go/bin/rekor-cli /usr/local/bin/
