docker stop loginflaskapp
docker rm loginflaskapp
docker build -t loginflaskapp .
docker tag loginflaskapp acobley/flaskapp
docker run -p 80:5000 -d --name loginflaskapp acobley/flaskapp
