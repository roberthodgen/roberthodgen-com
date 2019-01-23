GIT_REV=$(shell git rev-parse --short HEAD)

build:
	@echo git rev: ${GIT_REV}
	@docker build --rm=false -t hugo-tmp-image .
	@docker create --name hugo-tmp hugo-tmp-image
	@docker cp hugo-tmp:/usr/src/hugo/public build
	@docker rm hugo-tmp
	@docker rmi hugo-tmp-image

.PHONY: clean
clean:
	@rm -rfd build
	@rm -f cloudfront-distribution.json
	@rm -f etag
	@rm -f updated-distribution.json

.PHONY: serve
serve:
	@docker run --rm=true -p=1313:1313 -v=$(shell pwd):/usr/src/hugo roberthodgen/hugo:0.53-extended serve --bind=0.0.0.0 --buildDrafts

.PHONY: deploy
deploy: build updated-distribution.json
	@aws s3 cp build s3://com.roberthodgen.www${GIT_REV} \
		--recursive \
		--exclude "*" \
		--include "*.js" \
		--include "*.css" \
		--cache-control "max-age=31536000"
	@aws s3 cp build s3://com.roberthodgen.www/${GIT_REV} \
		--recursive \
		--exclude "*" \
		--include "*.html" \
		--cache-control "no-cache"
	@aws s3 cp build s3://com.roberthodgen.www/${GIT_REV} \
		--recursive \
		--exclude "*.js" \
		--exclude "*.css" \
		--exclude "*.html" \
		--cache-control "max-age=86400"
	@aws configure set preview.cloudfront true
	@aws cloudfront update-distribution --distribution-config=file://updated-distribution.json --id=${CLOUDFRONT_DISTRIBUTION_ID} --if-match=$(shell cat etag) 2>&1
	@aws cloudfront create-invalidation --distribution-id=${CLOUDFRONT_DISTRIBUTION_ID} --paths="/*" 2>&1

cloudfront-distribution.json:
	@aws configure set preview.cloudfront true
	@aws cloudfront get-distribution-config --id=${CLOUDFRONT_DISTRIBUTION_ID} >cloudfront-distribution.json 2>&1

etag:
	@python scripts/get-etag.py > etag 2>&1

updated-distribution.json: cloudfront-distribution.json etag
	@python scripts/update-origin.py ${GIT_REV} 2>&1
