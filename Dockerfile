# Use an official and lightweight Python 3.9 runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
# This is done first to leverage Docker's cache for faster builds
COPY requirements.txt .

# Install the necessary packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project's local directory into the container
# This includes app.py, models/, and src/ folders
COPY . .

# Expose port 5001 for the Flask application
# We use 5001 to bypass the macOS 403 Forbidden error on port 5000
EXPOSE 5001

# Define the command to run your app using the Python interpreter
CMD ["python", "app.py"]