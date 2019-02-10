.PHONY: env run test

ifndef PYVERSION
PYVERSION=3
endif

ifndef APIXUKEY
$(error APIXUKEY is not set)
endif

IMAGE=python:$(PYVERSION)-alpine
TEST_CMD := 'python setup.py install && pip install -r requirements-dev.txt && pytest'

env:
	docker run --rm -ti -v $(CURDIR):/src -w /src -e APIXUKEY=$(APIXUKEY) $(IMAGE) sh

run:
	docker run --rm -ti -v $(CURDIR):/src -w /src -e APIXUKEY=$(APIXUKEY) $(IMAGE) sh -c 'python setup.py develop && sh -c "python $(FILE)"'

test:
	docker run --rm -ti -v $(CURDIR):/src -w /src -e APIXUKEY=$(APIXUKEY) $(IMAGE) sh -c $(TEST_CMD)
