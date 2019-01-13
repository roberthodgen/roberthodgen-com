ifeq (, $(shell which docker))
	$(error "docker not in $(PATH)!")
endif

.PHONY: build
build: clean
	@docker run --rm=true -v=$(shell pwd):/usr/src/hugo roberthodgen/hugo

.PHONY: clean
clean:
	@rm -rfd public

.PHONY: serve
serve:
	@docker run --rm=true -p=1313:1313 -v=$(shell pwd):/usr/src/hugo roberthodgen/hugo serve --bind=0.0.0.0
