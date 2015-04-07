## My Personal site

> Static site which is served on http://www.roberthodgen.com

Based upon the theme: https://github.com/IronSummitMedia/startbootstrap-landing-page

__Still a work in-progress!__


#### Premise

To help a few people who asked me how to create a static site on GAE.


#### How it works

All static files (your HTML, CSS, etc.) are stored in the `/static` directory.

Our `app.yaml` file is configured to serve `/static` at our root (e.g. `http://www.roberthodgen.com/`). Any HTML or CSS files requested will be served (e.g. `/static/css/bootstrap.css` from `http://www.roberthodgen.com/css/bootstrap.css`).

We've created an additional rule (see below) that matches any folder requests (e.g. `http://www.roberthodgen.com/about`) to an `index.html` file stored within that directory in `/static` (e.g. `/static/about/index.html`). _Trailing slashes optional._

``` yaml
# Additional rule
- url: /([a-zA-Z0-9-_]+)/?
  static_files: static/\1/index.html
  upload: static/.*/index.html
```


#### Limitations:

- No 404 error when requested page not found
