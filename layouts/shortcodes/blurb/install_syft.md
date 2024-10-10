[Syft](https://github.com/anchore/syft) is a CLI tool for generating a Software Bill of Materials (SBOM). It is created and maintained by Anchore.

The recommended way to install Syft is by running a provided [installation script](https://github.com/anchore/syft/blob/main/install.sh). We recommend inspecting this script before running it on your local machine.

The following command will download the installation script and install Syft to your `/usr/local/bin` folder. Depending on your machine's configuration, you may need to add `sudo` at the beginning of the second line of the below command or otherwise use elevated permissions to complete the installation.

```sh
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | \
 sh -s -- -b /usr/local/bin
```

Alternately, your can install Syft with Homebrew:

```sh
brew install syft
```

You can also use Syft directly by pulling and running  the official image from Docker Hub. The following command will pull the Syft image and use it to scan the offical Python image from Dockerhub:

```sh
docker run -it anchore/syft:latest python
```

For more on installing Syft, review the project's installation [instructions on GitHub](https://github.com/anchore/syft#installation).
