# Use the official Python image
FROM python:3.10

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install the ODBC Driver 17 and other dependencies
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    msodbcsql17 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]

