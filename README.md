# Chainguard Academy

Our mission is to provide education on software supply chain security. 

Visit our website at [edu.chainguard.dev](https://edu.chainguard.dev)

You can find the educational resource files in markdown under the `content` directory.

## Development

This site is based off of the [Doks Hugo theme](https://github.com/h-enk/doks). 

If you would like to develop this project clone this repo and install dependencies with npm. 

```sh
npm install
```

To run a local version of this site, use npm to start it.

```sh
npm run start
```

You'll then navigate to `localhost:1313` within the web browser of your choice. 

## Contributing

If you identify something that is a major change, please file an [issue](https://github.com/chainguard-dev/edu/issues/new). If you identify a minor change like a typo that needs to be updated, or tech tooling that has a newer package, you are welcome to open a pull request for review from the team.

### Date Format

In each post's header, the date format should follow year-month-day as `YYYY-MM-DD`.

### Adding Images

Please reduce the image's file size prior to adding the image to this project to make page loadtimes faster and more accessible. You can use a tool such as [TinyPNG](https://tinypng.com/). 

If you are using images, it's best to bundle it together with the appropriate markdown file. Create a directory with the name of the new page. Within the directory, create an `index.md` file and add the images within the directory as well.

In practice, this will look like the following, with images in place for both the `getting-started-enforce-github` directory and the `install-enforce-github` directory and the relevant tutorials:

```
├── chainguard
│   ├── _index.md
│   ├── enforce-github
│   │   ├── _index.md
│   │   ├── getting-started-enforce-github
│   │   │   ├── check.png
│   │   │   ├── index.md
│   │   │   ├── protected-branch.png
│   │   │   └── repo-access.png
│   │   └── install-enforce-github
│   │       ├── configure.png
│   │       ├── index.md
│   │       ├── permissions.png
│   │       └── user-select.png
```

Within the markdown file, add images like so, with the alt text at the front:

```
![Protect branches with Chainguard Enforce](protected-branch.png)
```

Run a local development environment to ensure that your file structure is set up as intended.

### Adding Videos

Use a liquid tag within markdown to embed a YouTube video. For example, if you would like to link to the YouTube video located at [https://www.youtube.com/watch?v=rqIcDrg1XOs](https://www.youtube.com/watch?v=rqIcDrg1XOs), you can pull the string after `v=` and use the following liquid tag on its own line within markdown.

```
{{< youtube rqIcDrg1XOs >}}
```

### Adding an Interactive Terminal

To include an interactive terminal in a given tutorial page, add the following line in the Hugo frontmatter:

```
academy/apko:latest
academy/chainguard-images:latest
academy/cosign:latest
academy/images-demos:latest
academy/rekor:latest
academy/vexctl:latest
policy-controller/base:latest
policy-controller/install:latest
```

The interactive terminal is under active development and not every tool is currently available within the environment.
