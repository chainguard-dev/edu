Our command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard Enforce provides, enabling you to make queries into the state of your clusters and policies.

Create a new directory called `enforce-demo`.

```sh
mkdir ~/enforce-demo && cd $_
```

To install `chainctl`, we’ll use the `curl` command to pull the application down.

```sh
curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/')"
```

Move `chainctl` into your `/usr/local/bin` directory and elevate its permissions so that it can execute as needed.

```sh
sudo install -o $UID -g $GID -m 0755 chainctl /usr/local/bin/chainctl
```

Finally, alias its path so that you can use `chainctl` on the command line.

```sh
alias chainctl=/usr/local/bin/chainctl
```

You can verify that everything was set up correctly by checking the `chainctl` version.

```sh
chainctl version
```

```
   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control
GitVersion:    bf36b2b
GitCommit:     bf36b2be08c0dca8e4d2174ee21c31b9679c4ece
GitTreeState:  clean
BuildDate:     2022-10-13T21:13:11Z
GoVersion:     go1.18.7
Compiler:      gc
Platform:      darwin/arm64
```

You can update `chainctl` at any time to ensure you have the most up-to-date version by running `chainctl update`.
