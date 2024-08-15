---
title: "Getting Started with the Ruby Chainguard Image"
linktitle: "Ruby"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-ruby
type: "article"
description: "Tutorial on how to get started with the Ruby Chainguard Image"
date: 2023-05-10T11:07:52+02:00
lastmod: 2023-05-10T11:07:52+02:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 065
toc: true
---

The [Ruby images](https://images.chainguard.dev/directory/image/ruby/versions) maintained by Chainguard are a mix of development and production distroless images that are suitable for building and running Ruby workloads.

Because Ruby applications typically require the installation of third-party dependencies via [Rubygems](https://rubygems.org/), using a pure distroless image for building your application would not work. In cases like this, you'll need to implement a [multi-stage Docker build](https://docs.docker.com/build/building/multi-stage/) that uses one of the `-dev` images to set up the application.

In this guide, we’ll build two example applications that demonstrate how to use Ruby container images based on [Wolfi](/open-source/wolfi/overview/) as a runtime. In the first, we’ll use a minimal image containing just Ruby to execute a demo that doesn't have any external dependencies. In the second example, we'll set up a multi-stage Docker build to run a demo that requires the installation of Rubygems via `bundler`.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Example 1: Minimal Ruby Image in Single Stage Build
We'll start by creating a small command-line Ruby application to serve as a demo. This application has no external dependencies; it will read from a text file containing facts about octopuses, and output a random line from that file. This demo is also available in our [demos repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/ruby), if you want to review the source files before building it.

### Step 1: Setting up the Application

First, create a directory and then move into it for your app. Here we'll use `octo-facts`:

```shell
mkdir ~/octo-facts && cd ~/octo-facts
```

Next, create a new file to serve as the application entry point. Here, we’ll use `octo.rb`. You can edit this file in whatever code editor you would like. We’ll use `nano` as an example.

```shell
nano octo.rb
```

The following Ruby code will read a random line from the `facts.txt` file and print it out to the terminal:

```ruby
#!/usr/bin/env ruby

class OctoFact
  attr_accessor :source

  def initialize(source = "facts.txt")
    @source = source
  end

  def random_line
    puts File.readlines(@source).sample
  end
end

if __FILE__ == $0
  fact = OctoFact.new
  fact.random_line
end
```
Copy this code to your `octo.rb` script, then save and close the file.

Next, pull down the `facts.txt` file with `curl`. You can [inspect the file's contents](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/ruby/octo-facts/facts.txt) before downloading it to ensure it is safe to do so. Make sure you are still in the same directory where your `octo.rb` script is.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/ruby/octo-facts/facts.txt
```

With all files in place, you can now run the demo using Docker. The following command will execute the demo code using the same base image we'll use to build our Dockerfile in the next step. It will set up a volume sharing the files in the current directory with the location `/work` inside the container, then execute the `octo.rb` script:

```shell
docker run --rm -v ${PWD}:/work cgr.dev/chainguard/ruby octo.rb
```

And you should get output like this, with a random fact about octopuses:

```shell
Octopuses have decentralized brains.
```

In the next step, we'll create a Dockerfile to build and run the demo.

### Step 2: Setting up the Dockerfile

With the demo ready, you can now set up a Dockerfile to build a custom image for your Ruby application. Make sure you're still on the same directory as the application files, then create a new Dockerfile using your text editor of choice:

```shell
nano Dockerfile
```

The following Dockerfile will:

1. Start a new image based on the `cgr.dev/chainguard/ruby:latest` image;
2. Set up a workdir at `/app`;
3. Copy the application files to the workdir;
4. Set up the entry point for the image as `ruby octo.rb`.

Copy the following content to your `Dockerfile`:

```Dockerfile
FROM cgr.dev/chainguard/ruby:latest

WORKDIR /app

COPY octo.rb facts.txt ./

ENTRYPOINT [ "ruby", "octo.rb" ]
```

Save and close the file when you're done. Next, build the image with:

```shell
docker build . -t octo-ruby-demo
```

Once the build is finished, you can execute the image with:

```shell
docker run --rm octo-ruby-demo
```

And you should get output similar to what you got before, with a random octopus fact.

## Example 2: Multi-Stage Build for Ruby Application Runtime

To demonstrate how to containerize a more complex application that requires the installation of third party dependencies, we'll create a second demo that uses a [Docker multi-stage build](https://docs.docker.com/build/building/multi-stage/), which will combine the `cgr.dev/chainguard/ruby:latest-dev` development image to build the application and the `cgr.dev/chainguard/ruby:latest` distroless image to run it.

This demo will use the [rainbow](https://rubygems.org/gems/rainbow) Ruby gem to output to the command line interface a colorful quote, inspired by _cowsay_.

### Step 1: Setting up the Application

First, create a directory for your app. Here we'll use `linky-says`:

```shell
mkdir ~/linky-says && cd ~/linky-says
```

Then, set up your Gemfile:

```shell
nano Gemfile
```

Copy the following content into your Gemfile to require the Rainbow Gem:

```ruby
source 'https://rubygems.org'

gem 'rainbow'
```
Save and close the file.

Next, create a new Ruby script file called `linky.rb`:

```shell
nano linky.rb
```

The following code outputs a colorful quote provided at runtime, incorporating an ASCII representation of Linky that is pulled from an `linky.txt` file located at the same directory as the ruby script. The printed quote colors alternate randomly between purple and magenta.

```ruby
#!/usr/bin/env ruby

require 'rainbow'
Rainbow.enabled = true

class Linky
  def says(message = "Hello World")
    colors = [:purple, :magenta]
    words = message.split(" ")

    print "\n ".ljust(40, " ")
    words.each do |n|
      print Rainbow(n).color(colors.sample) + " "
    end

    print "\n"
    puts File.readlines('linky.txt')
  end
end

if __FILE__ == $0
  linky = Linky.new
  inputArray = ARGV
  message = inputArray.length > 0 ? inputArray.join(' ') : "Hello Wolfi"
  linky.says(message)
end
```

Copy this code to your `linky.rb` script, then save and close the file.

Next, pull down the ASCII `linky.txt` file with `curl`. You can [inspect the file contents](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/ruby/linky-says/linky.txt) before downloading it to ensure it is safe to do so. Make sure you are still in the same directory where your `linky.rb` script is.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/ruby/linky-says/linky.txt
```

With everything in place, you can now work on the Dockerfile that will install the application dependencies and execute your Ruby script.

### Step 2: Setting Up the Dockerfile

To make sure our final image is _distroless_ while still being able to install Rubygems, our build will consist of **two** stages: first, we'll build the application using the `dev` image variant, a Wolfi-based image that includes the Gem executable, Bundler, and other useful tools for development. Then, we'll create a separate stage for the final image. The resulting image will be based on the distroless Ruby Wolfi image, which means it doesn't come with the Gem executable or even a shell.

Create a new Dockerfile using your code editor of choice, for example `nano`:

```shell
nano Dockerfile
```
The following Dockerfile will:

1. Start a new build stage based on the `cgr.dev/chainguard/ruby:latest-dev` image and call it `builder`;
2. Set up environment variables that define the default location of installed Gems;
3. Copy the Gemfile from the current directory to the `/work` location in the container;
4. Install Bundler and run `bundle install`;
5. Start a new build stage based on the `cgr.dev/chainguard/ruby:latest` image;
6. Set up environment variables that define the default location of installed Gems;
7. Copy build artifacts from `builder` and into the final image
8. Copy the `linky.rb` and `linky.txt` files into the final image
9. Set up the application entry point as `ruby linky.rb`.

Copy this content to your own `Dockerfile`:

```Dockerfile
FROM cgr.dev/chainguard/ruby:latest-dev as builder

ENV GEM_HOME=/work/vendor
ENV GEM_PATH=${GEM_PATH}:/work/vendor
COPY Gemfile /work/
RUN gem install bundler && bundle install

FROM cgr.dev/chainguard/ruby:latest

ENV GEM_HOME=/work/vendor
ENV GEM_PATH=${GEM_PATH}:/work/vendor

COPY --from=builder /work/ /work/
COPY linky.rb linky.txt /work/

ENTRYPOINT [ "ruby", "linky.rb" ]

```
Save the file when you're finished.

You can now build the image with:

```shell
docker build . -t linky-says
```

Once the build is finished, run the image with:

```shell
docker run --rm linky-says Wolfi says hi
```

And you should get output like this:

```

                                       Wolfi says hi
                   @@@
              @@@*******@@@              /
           @@%**@@@@*******@@@          /
          @@*@@***********///@@        /
         @*************///////&@      /
        @@*****%@@@**////@@@&//@@    /
        @*****@**##@////@//##@//@   /
        @@*****@@@@//////@@@@//@@  /
      ,@@@@***////////////////@@@@,
 @@@*******/////////////////////(((((@@@
 @*******//////////////////////((((((((@
    @@@/////////@///////@///(((((%@@@
     #@///////@@@///////@@@((((((#@
         @@@    /@@///@@,    @@@

```

If you inspect the image with a `docker image inspect linky-says`, you'll notice that it has only **three** layers, thanks to the use of a multi-stage Docker build.

```shell
docker image inspect linky-says
```
```shell
...
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ec653fe8da922557dd1d78b47b2c0074a6e9257e5a15e596bc4e1fb1e325c3d8",
                "sha256:d9541a2e82274d8140ed7f4cc79ce92f295d13951585c4a433f1baa35015e1eb",
                "sha256:a44e5fee28e11702a63418bf76c009b1b4948f1b0426e0f199b83702ae187796"
            ]
        },
        "Metadata": {
            "LastTagTime": "2023-05-09T19:53:16.060125796+02:00"
        }
    }
]

```
In such cases, the last `FROM` section from the Dockerfile is the one that composes the final image. That's why in our case it only adds two layers on top of the base `cgr.dev/chainguard/ruby:latest` image, containing the two `COPY` commands we use to copy the application files and its dependencies to the final image.

It's worth highlighting that no code or data is carried from one stage to the other unless you use a `COPY` command to explicitly copy it. This approach facilitates creating a slim final image with only what's absolutely necessary to execute the application. Using a multi-stage build like this, without shell tools and interactive language interpreters built in also makes your final image more secure.

## Advanced Usage

{{< blurb/images-advanced image="Ruby" >}}

