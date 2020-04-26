.PHONY: test

deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt


lint:
	flake8 hello_world test


test:
	PYTHONPATH=. py.test


run:
	PYTHONPATH=. FLASK_APP=hello_world flask run

docker_build:
	docker build -t 'hello_ap_printer' .

docker_clean:
	docker rm -f 'helloprinter'

docker_run: docker_build docker_clean
	docker run \
		--name 'helloprinter' \
		-p 5000:5000 \
		-d hello_ap_printer
