# Flask-Docker-App
Creating Flask Docker app through EC2 instance:

## Commands to create Flask Docker app through EC2 instance:
- Create an EC2 instance and connect
```
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
touch dockerfil
ls -ltrh
vi app.py
```               
   
## Add below content in file1 :
```
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return "Hello from Flask in Docker! Creating first Docker application through EC2"
 
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)
```
   
## add below content in file2
```
vi dockerfile
```
```
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask 
# Run the Flask app
CMD ["python", "app.py"]
```
```
cat app.py
cat dockerfile
docker build -t flask-docker-app .
docker images
docker run -d -p 5000:5000 flask-docker-app
```
**Now check with public ip of instance "public ip:5000" to get the result as "Hello from Flask in Docker! Creating first Docker application through EC2"**

