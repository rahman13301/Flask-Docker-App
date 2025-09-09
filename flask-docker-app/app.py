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

