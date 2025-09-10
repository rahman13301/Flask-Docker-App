# Flask-Docker-App
Creating Flask Docker app through EC2 instance:

## Commands to create Flask Docker app through EC2 instance:

### Create an EC2 instance and connect, commands to install docker and check docker status.
```
sudo yum update
sudo yum install -y docker
docker --version 
systemctl status docker
systemctl start docker
systemctl status docker
```
<img width="740" height="66" alt="image" src="https://github.com/user-attachments/assets/550f2502-aee7-49d5-a824-0866792819fb" />

<img width="910" height="226" alt="image" src="https://github.com/user-attachments/assets/6b840f60-13f1-48bf-bfc8-88562a75c08e" />

### Create files inside directory "app.py" and "dockerfile" 
```
mkdir flask-docker-app
cd flask-docker-app
touch app.py
touch dockerfile
ls -ltrh
vi app.py
```
<img width="651" height="128" alt="image" src="https://github.com/user-attachments/assets/d8880b25-952f-4853-a930-c2f3ae5f80f0" />
              
   
### Add below content in app.py :
```
from flask import Flask

 app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask in Docker! Creating first Docker application through EC2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
   
### Add below content in dockerfile:
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

<img width="926" height="543" alt="image" src="https://github.com/user-attachments/assets/14cfa017-022b-4621-adcc-31bd1de01d74" />

### Verify code, commands for docker build and docker run:

```
cat app.py
cat dockerfile
sudo docker build -t flask-docker-app .
sudo docker images
sudo docker run -d -p 5000:5000 flask-docker-app
```
<img width="984" height="188" alt="image" src="https://github.com/user-attachments/assets/3d098624-55a7-463f-9a95-15ae32f85de9" />

<img width="832" height="145" alt="image" src="https://github.com/user-attachments/assets/7443bc41-6823-4883-87f7-7fb54a9035d5" />


- **Note** : We will have to edit the inbound rules in the security group of our EC2, in order to allow traffic from our particular port like (port 5000 in this project).
<img width="1784" height="377" alt="image" src="https://github.com/user-attachments/assets/d077bd1b-d10e-4526-8f29-2ce4a0df584a" />




- Browse with public ip of instance "public ip:5000" to get the result


