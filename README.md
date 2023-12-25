# Gogolook test
## Run in test mode
```bash
flask --app src/main.py --debug run
```

## Build Docker Image
```bash
IMAGE_TAG=gogolook:latest \
bash build.sh
```

## Run Docker
```bash
docker run -d --name flask_app -p 80:80 $IMAGE_TAG
```