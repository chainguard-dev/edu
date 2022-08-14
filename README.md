# Chainguard Academy

Our mission is to provide education on software supply chain security. 

TODO: visit our website at [edu.chainguard.dev]()

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

### Adding Images

Please reduce the image's file size prior to adding the image to this project to make page loadtimes faster and more accessible. You can use a tool such as [TinyPNG](https://tinypng.com/). 

Place images within the `/static` directory. This is organized by folders that mirror the folders of the `/content` directory. 

Add images with an HTML tag and use `alt` text:

```
<img src="/static/image.png" alt="image description">
```

Use the absolute path, as above, for the image link. 

### Adding Videos

Use a liquid tag within markdown to embed a YouTube video. For example, if you would like to link to the YouTube video located at [https://www.youtube.com/watch?v=rqIcDrg1XOs](https://www.youtube.com/watch?v=rqIcDrg1XOs), you can pull the string after `v=` and use the following liquid tag on its own line within markdown.

```
{{< youtube rqIcDrg1XOs >}}
```