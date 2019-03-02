FROM roberthodgen/hugo:0.53-extended AS builder

COPY . /usr/src/hugo

RUN hugo --minify
