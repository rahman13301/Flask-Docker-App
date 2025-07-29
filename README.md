# Flask-Docker-App
Create Flask Docker app through EC2 instance:

**Commands to create Flask Docker app through EC2 instance**
Step1 : Create an EC2 instance and connect
    1  **yum install -y docker**        : command to install docker in server
    2  **docker --version**             : command to check the docker version 
    3  **systemctl status docker**      : command to check the status of docker
    4  **systemctl start docker**       : command to start the docker
    5  **systemctl status docker**
    6  **docker info**                  : to check detailed info about docker
    7  **cd /home**                     : switch to home directory
    9  **mkdir flask-docker-app/**      : create a new directory
   10  **cd flask-docker-app/**         : switch to new directory
   12  **touch app.py**                 : create a new file1
   13  **touch dockerfile**             : create a new file2
   14  **ls -ltrh**                     : list files created
   15  **vi app.py**                    : add contect in file1                    
   
**Add below content in file1 :**

**from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return "Hello from Flask in Docker! Creating first Docker application through EC2"
 
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)**
   


16  **vi dockerfile**		                            : add content in file2 

**Add below content in file2:**

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

   17  **cat app.py**                                      : verify the content of file1
   18  **cat dockerfile**                                  : verify the content of file2
   19  **docker build -t flask-docker-app .**              : to build the docker image
   20  **docker images**                                   : to verify docker images
   21  **docker run -d -p 5000:5000 flask-docker-app**     : to run the docker image

   **Now check with public ip of instance "public ip:5000" to get the result as "Hello from Flask in Docker! Creating first Docker application through EC2"**

