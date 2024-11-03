# Dockerfile

# Base image with Python
FROM python:3.12-slim

# Install Tesseract OCR
RUN apt-get update && \
    apt-get install -y zbar-tools libzbar0 && \
    apt-get clean

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
