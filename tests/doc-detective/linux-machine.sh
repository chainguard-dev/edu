#!/usr/bin/env bash
# Gives shell tests a disposable Linux machine, so installing chainctl the way
# a page describes never touches the chainctl on the machine running the tests.
#
#   linux-machine.sh start NAME [OPTION...]
#       Starts a container named NAME, replacing any left over from an earlier
#       run. Without options it's a bare Ubuntu with a sudo user named dev.
#       --packages "curl jq"   apt packages to install
#       --cosign               install the latest Cosign release
#       --chainctl VERSION     install that chainctl release to /usr/local/bin
#       --brew                 use Homebrew's image and its linuxbrew user
#                              instead; other options don't apply
#   linux-machine.sh run NAME [DIR] [--answer TEXT]
#       Runs the commands on stdin with bash -e as the machine's user, from
#       DIR relative to their home directory (default: home). With --answer,
#       the commands read TEXT as their input, for answering a prompt.
#   linux-machine.sh stop NAME
#
# A container stops on its own after 30 minutes, so a failed test that never
# reaches its stop step doesn't leave it running.
set -euo pipefail

command="${1:?usage: linux-machine.sh start|run|stop NAME}"
name="${2:?usage: linux-machine.sh start|run|stop NAME}"
shift 2

case "$command" in
  start)
    image="ubuntu:24.04" user="dev" packages="" cosign="" chainctl=""
    while [ "$#" -gt 0 ]; do
      case "$1" in
        --packages) packages="$2"; shift 2 ;;
        --cosign) cosign=1; shift ;;
        --chainctl) chainctl="$2"; shift 2 ;;
        --brew) image="homebrew/brew:latest" user="linuxbrew"; shift ;;
        *) echo "unknown option: $1" >&2; exit 2 ;;
      esac
    done
    docker rm -f "$name" >/dev/null 2>&1 || true
    docker run -d --rm --name "$name" --label "doc-detective.user=$user" \
      --entrypoint sleep "$image" 1800 >/dev/null
    if [ "$user" = "linuxbrew" ]; then
      exit
    fi
    docker exec -i "$name" bash -e -s <<EOF
apt-get update -qq
apt-get install -y -qq sudo ca-certificates $packages >/dev/null
useradd -m -s /bin/bash dev
echo "dev ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/dev
if [ -n "$cosign" ]; then
  curl -fsSLo /usr/local/bin/cosign https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64
  chmod 0755 /usr/local/bin/cosign
fi
if [ -n "$chainctl" ]; then
  curl -fsSLo /usr/local/bin/chainctl https://dl.enforce.dev/chainctl/$chainctl/chainctl_linux_x86_64
  chmod 0755 /usr/local/bin/chainctl
fi
EOF
    ;;
  run)
    dir="" answer=""
    while [ "$#" -gt 0 ]; do
      case "$1" in
        --answer) answer="$2"; shift 2 ;;
        *) dir="$1"; shift ;;
      esac
    done
    user="$(docker inspect -f '{{index .Config.Labels "doc-detective.user"}}' "$name")"
    script="$(cat)"
    printf '%s\n' "$answer" |
      docker exec -i -u "$user" "$name" bash -c 'cd ~/"$1" && exec bash -e -c "$2"' _ "$dir" "$script"
    ;;
  stop)
    docker rm -f "$name" >/dev/null
    ;;
  *)
    echo "unknown command: $command" >&2
    exit 2
    ;;
esac
