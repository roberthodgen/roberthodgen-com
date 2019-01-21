---
title: "Personal site rewrite using Hugo"
date: 2019-01-21T15:32:42-05:00
---

This site was rewritten--welcome to my new personal site!

It's built using [Hugo a static site generator](https://gohugo.io/). Based off Markdown files for each page's content. The metadata is stored alongside the content and Hugo knows how to generate each page based off its location, [front-matter](https://gohugo.io/content-management/front-matter/), and a [site-wide theme](#theme).

### Why?

I've always been interested in having a simple and easy to maintain personal site. Markdown files have always intrigued me as great for this purpose.

### Goals

- Speed, it's gotta load fast
- No database, store everything as files
- Dead nuts simple

### What came before this?

Way back in the day I ran a Wordpress site. It was a bit overpowered for my personal site. There wasn't that much content to manage and there wasn't enough benefit IMO to offset the extra overhead of managing an install of Wordpress. The themes were great however!

### Prior work

My first attempt at a rewrite was an AngularJS and Python site. It read from a `/content` directory and looked for files like:

```
.
+-- content
|   +-- hello-world
|       +-- manifest.json
|       +-- content.md
|   +-- post-two
|       +-- manifest.json
|       +-- content.md
```

The Python server would read the `/content` directory traversing each subdirectory compiling a list of `manifest.json` files. It would combine these into a JSON object like:

```json
[{
  "title": "Hello world",
  "path": "/hello-world",
  "date": "...",
  "summary": "...",
}, {
  "title": "Post Two",
  "path": "/post-two",
  "date": "...",
  "summary": "...",
}]
```

The AngularJS front-end webapp would read the JSON and build out the site.

This however required extra overhead. While I liked the idea of reusable content it wasn't perfect:

**Pros:**

- Content written as Markdown
- Very quick once loaded

**Cons:**

- Unneeded complexity from building/maintaining single page webapp
- Longer load time for AngularJS library and app code
- Had to run a Python server
- Separate `manifest.json` file for metadata

### Why Hugo?

I decided to use Hugo after working with it at [Auto Data Direct]({{< ref "/experience/auto-data-direct" >}}). I was involved with moving from a Drupal site to Hugo. I liked how well it worked and because it was so similar to my original goals I gave it a shot.

### How does Hugo work?

Hugo reads my static content files (written in Markdown) and builds the HTML based off their location, metadata, and a site-write theme.

### Theme

I rolled my own theme, it is based off the _work in progress_ AngularJS project I mentioned above. It features a "hero image" of me and is based off Bootstrap.

I know [Bootstrap](https://getbootstrap.com/) well so using it felt like a natural choice.

Hugo allows you to choose, create, and share themes. I highly suggest looking into it: https://themes.gohugo.io/

### Tools

I made a Docker image for this purpose, see: https://hub.docker.com/r/roberthodgen/hugo

Docker pull command:

```
$ docker pull roberthodgen/hugo
```

This image contains the `hugo` command so it's not necessary to keep it up to date on my local machine.

Look at this repo's `Makefile` and `Dockerfile`. They work together to generate this site. More of that coming soon...
