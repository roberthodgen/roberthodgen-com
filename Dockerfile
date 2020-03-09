FROM roberthodgen/hugo:0.67.0-extended AS builder

COPY . /usr/src/hugo

RUN hugo --minify
