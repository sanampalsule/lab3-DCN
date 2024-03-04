# Sanam Palsule - sp7940
#Use  a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 53533 available 
EXPOSE 53533

# Run the as.py when the container launches
CMD ["python", "as.py"]
