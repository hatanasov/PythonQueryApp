# Python Query App

A lightweight Python application that monitors external URLs, measures response times, and exposes metrics in Prometheus format.

## Features

- Monitors HTTP endpoints for availability (status 200)
- Measures response times in milliseconds
- Exposes Prometheus metrics at `/metrics`
- Configurable via environment variables
- Docker containerized
- Kubernetes deployment via Helm

## Quick Start

### Local Development

```bash
# Clone repository
git clone <repository-url>
cd PythonQueryApp

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
export URLS="https://google.com,https://httpstat.us/503"
python QueryApp/main.py

# View metrics
curl http://localhost:9100/metrics
```

### Docker

```bash
# Build image
docker build -t python-query-app .

# Run container
docker run -p 9100:9100 -e URLS="https://google.com,https://httpstat.us/503" python-query-app
```

### Kubernetes with Helm

```bash
# Install chart
helm repo add my-app-repo https://hatanasov.github.io/PythonQueryApp/

# search for the package in the repo
helm search repo python-query-app

# Install from repo
helm install quert-app python-query-app/python-query-app

# or provide custom values file
helm install quert-app python-query-app/python-query-app -f values.yaml 
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `URLS` | `""` | Comma-separated URLs to monitor |
| `PORT` | `9100` | HTTP server port (hardcoded in app) |

## Metrics

The application exposes these Prometheus metrics:

- `external_url_up{url="..."}` - URL availability (1=up, 0=down)
- `external_url_response_ms{url="..."}` - Response time in milliseconds

## Helm Chart Values

Key configuration options:

```yaml
replicaCount: 1

image:
  repository: hristoatanasov87/url_check_app_arm64
  tag: "0.1.0"

env:
  - name: URLS
    value: "https://google.com,https://google.com/400"

service:
  type: ClusterIP
  port: 9100

ingress:
  enabled: false
```

## Requirements

- Python 3.13+
- Docker 20+ (for containerization)
- Kubernetes cluster (for deployment)
- Helm 3+ (for chart deployment)

## Architecture

The application runs a simple loop that:
1. Checks each configured URL every 60 seconds
2. Records HTTP status and response time
3. Updates Prometheus metrics
4. Serves metrics on `/metrics` endpoint