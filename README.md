# Flask-Docker-App
Creating Flask Docker app through EC2 instance:

## Commands to create Flask Docker app through EC2 instance:
- Create an EC2 instance and connect, commands to install docker, create directory, create files in directory "app.py" and "dockerfile" 
```
sudo apt update
yum install -y docker
docker --version 
systemctl status docker
systemctl start docker
systemctl status docker
docker info
cd /home
mkdir flask-docker-app
cd flask-docker-app
touch app.py
touch dockerfile
ls -ltrh
vi app.py
```               
   
## Add below content in app.py :
```
from flask import Flask

 app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask in Docker! Creating first Docker application through EC2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
   
## Add below content in dockerfile:
```
vi dockerfile
```
```
# Use official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the local files to container
COPY . /app

# Install Flask inside container
RUN pip install flask

# Run the Flask app
CMD ["python", "app.py"]
```
## Verify code, commands for docker build and docker run:
```
cat app.py
cat dockerfile
docker build -t flask-docker-app .
docker images
docker run -d -p 5000:5000 flask-docker-app
```
**Now check with public ip of instance "public ip:5000" to get the result as "Hello from Flask in Docker! Creating first Docker application through EC2"**

