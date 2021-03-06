stages:
- test
- docker_build

test:
  image: "python:3"
  stage: test
  script:
  - pip install -r requirements.txt
  - pip install -r test_requirements.txt
  - PYTHONPATH=. py.test  --verbose -s
docker:
  image: docker:stable
  services:
    - docker:dind
  stage: docker_build
  script:
  - docker build -t myapp .
