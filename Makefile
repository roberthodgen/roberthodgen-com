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
	@rm -f update-distribution.json

.PHONY: serve
serve:
	@docker run --rm=true -p=1313:1313 -v=$(shell pwd):/usr/src/hugo roberthodgen/hugo:0.53-extended serve --bind=0.0.0.0 --buildDrafts

.PHONY: deploy
deploy: build update-distribution.json
	@echo "Beginning S3 synchronization..."
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
	@echo "Synchronized."
	@aws configure set preview.cloudfront true
	@aws cloudfront update-distribution --distribution-config=file://update-distribution.json --id=E2ZKY8YC7GKC4C --if-match=$(shell cat etag) 2>&1
	@aws cloudfront create-invalidation --distribution-id=E2ZKY8YC7GKC4C --paths="/*" 2>&1
	@echo "Deploy done."

cloudfront-distribution.json:
	@echo "Beginning CloudFront distribution config fetch..."
	@aws configure set preview.cloudfront true
	@aws cloudfront get-distribution-config --id=E2ZKY8YC7GKC4C >cloudfront-distribution.json 2>&1
	@echo "Fetched cloudfront-distribution.json."

etag:
	@echo "Beginning ETag retrieval..."
	@python scripts/get-etag.py
	@echo "Retrieved ETag. etag:"
	@cat etag

update-distribution.json: cloudfront-distribution.json etag
	@echo "Beginning distribution configuration transformation..."
	@python scripts/update-origin.py ${GIT_REV} 2>&1
	@echo "Transformed. update-distribution.json:"
	@cat update-distribution.json
