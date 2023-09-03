# jenkins_study

```bash
# https://github.com/zsu58/docker_files/tree/main/jenkins
docker build -t jenkins-blueocean .
docker network create jenkins
docker run --name jenkins-blueocean \
  -d \
  --restart=on-failure \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  jenkins-blueocean:latest
```