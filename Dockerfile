FROM python:3.13-slim

# Working directory inside container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies without cache to keep image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY QueryApp/ .

# Expose the port your app listens on (Prometheus will scrape this)
EXPOSE 9100

# Set environment variables
# ENV URLS="https://google.com/500,https://google.com"

# Run the application
CMD ["python", "main.py"]
