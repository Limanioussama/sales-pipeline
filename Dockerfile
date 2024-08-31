# Use the official Python image from Docker Hub as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run your script when the container starts
CMD ["python", "./scripts/extract.py"]
