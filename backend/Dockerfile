# Use the official Python image from DockerHub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 to make it accessible to other containers
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
