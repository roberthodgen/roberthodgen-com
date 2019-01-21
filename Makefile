ifeq (, $(shell which docker))
	$(error "docker not in $(PATH)!")
endif

.PHONY: build
build: clean
	@docker build --rm=false -t hugo-tmp-image .
	@docker create --name hugo-tmp hugo-tmp-image
	@docker cp hugo-tmp:/usr/src/hugo/public public
	@docker rm hugo-tmp
	@docker rmi hugo-tmp-image

.PHONY: clean
clean:
	@rm -rfd public

.PHONY: serve
serve:
	@docker run --rm=true -p=1313:1313 -v=$(shell pwd):/usr/src/hugo roberthodgen/hugo:0.53-extended serve --bind=0.0.0.0
