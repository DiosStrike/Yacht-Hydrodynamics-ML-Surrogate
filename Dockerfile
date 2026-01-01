# Use a modern Python runtime to support latest library versions
FROM python:3.11-slim

# Set the working directory for the container
WORKDIR /app

# Copy only requirements first to optimize Docker layer caching
COPY requirements.txt .

# Install dependencies without pinning to problematic local versions
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose port 5001 for public access
EXPOSE 5001

# Start the application using gunicorn for production stability
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]