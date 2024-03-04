# Sanam Palsule - sp7940
#Use an official Python runtime as a parent image
FROM python:3.9-slim

# set working dir
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install requirements
RUN pip install Flask requests

# Make port 8080 available
EXPOSE 8080

# Run us.py when the container launches
CMD ["python", "us.py"]


