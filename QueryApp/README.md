# Python External URL Monitoring App

This is a Python application that monitors external URLs, checks their availability, measures response times, and exposes metrics in **Prometheus format**. The application is containerized with Docker and can be deployed on a Kubernetes cluster using Helm.

---

## Features

- Periodically checks a list of URLs for HTTP status `200`.  
- Measures response time in milliseconds.  
- Exposes Prometheus-compatible metrics at `/metrics` endpoint.  
- Fully configurable via environment variables.  
- Docker-ready for easy deployment on Kubernetes or other container platforms.

---

## Prerequisites

- Python 3.13+  
- Docker 20+ (for local containerization)  
- Kubernetes cluster (optional, for deployment)  
- Helm 3+ (optional, for deployment)  

---

## Environment Variables

| Variable | Default                                           | Description |
|----------|---------------------------------------------------|-------------|
| `URLS`  | `https://httpstat.us/200,https://httpstat.us/503` | Comma-separated list of URLs to monitor |
| `PORT`  | `9100`                                            | Port where the HTTP server exposes metrics |

---

## Running Locally

### 1. Clone the repository

```bash
git clone git@github.com:hatanasov/PythonQueryApp.git
cd PythonQueryApp
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the application

```bash
export URLS="https://httpstat.us/200,https://httpstat.us/503"
python QueryApp/main.py
```

### 5. Get prometheus metrics

```commandline
curl http://localhost:9100/metrics
```

