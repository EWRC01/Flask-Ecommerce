# Use the official Python base image
FROM python:3.11.1-alpine3.17

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the entrypoint command for the container
CMD ["python", "app.py"]
