ifeq (, $(shell which docker))
	$(error "docker not in $(PATH)!")
endif

DOCKER_IMAGE=roberthodgen/hugo:0.53-extended

.PHONY: build
build: clean
	@docker run --rm=true -v=$(shell pwd):/usr/src/hugo ${DOCKER_IMAGE}

.PHONY: clean
clean:
	@rm -rfd public

.PHONY: serve
serve:
	@docker run --rm=true -p=1313:1313 -v=$(shell pwd):/usr/src/hugo ${DOCKER_IMAGE} serve --bind=0.0.0.0
