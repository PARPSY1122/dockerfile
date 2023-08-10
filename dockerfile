# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py .

# Install Flask
RUN pip install Flask

# Expose port 5000
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
