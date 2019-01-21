FROM scratch AS source

COPY . /usr/src/hugo

FROM roberthodgen/hugo:0.53-extended AS builder

COPY --from=source /usr/src/hugo .

RUN hugo
