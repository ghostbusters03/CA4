# Use Python Alpine image as base image
FROM python:3.13.0a4-alpine3.19

# Creating directory for the application source code
RUN mkdir -p /app

# Copy the source code of the application into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Print the current working directory 
RUN pwd

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Specify the command to run the application
CMD ["python", "app.py"]