## Interactive Terminal Dockerfiles

The directories and files in here are used to generate container images on the Academy site. Images are derived from the `academy-base` image, which includes things like `curl`, `tmux`, `jq`, and `nano`. 

Derived images only need to set a Docker `CMD` to override the default `sleep 3600` command that is passed to the image on start up.
