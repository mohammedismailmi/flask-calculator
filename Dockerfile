# Use Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files to container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
