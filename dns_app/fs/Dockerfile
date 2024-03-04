# Sanam Palsule - sp7940
#Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory 
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install requirements
RUN pip install Flask

# Make port 9090 available to the world outside this container
EXPOSE 9090

# Run fs.py when the container launches
CMD ["python", "fs.py"]
