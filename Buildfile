docker stop loginflaskapp
docker rm loginflaskapp
docker build -t loginflaskapp .
docker tag loginflaskapp https://github.com/veraborvinski/loginflaskapp
docker run -p 80:5000 -d --name loginflaskapp https://github.com/veraborvinski/loginflaskapp
