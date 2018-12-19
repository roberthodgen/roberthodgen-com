# roberthodgen-com
> Personal site.

Live site: http://www.roberthodgen.com/

## Info

Static site built using [Hugo](https://gohugo.io/) and hosted using Google Cloud Storage.

## Building

Built using [Hugo](https://gohugo.io/), last built using Hugo 0.52.

Run the `hugo` command:

```
$ hugo
```

This results in the static site being built into the `/public` directory.

## Deploying

Sync up to Google Cloud Storage, e.g.:

```
$ gsutil rsync -R public gs://www.roberthodgen.com
```

// TODO: get Travis CI working on any merge or push to master

## Developing

Run a Hugo development server:

```
$ hugo serve -D
```

Visit http://localhost:1313 :)

## Theme

// TODO
