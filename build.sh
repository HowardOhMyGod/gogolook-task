IMAGE_TAG="${IMAGE_TAG:=gogolook:latest}"

poetry export --without-hashes --format=requirements.txt > requirements.txt && \
docker build -t $IMAGE_TAG .
