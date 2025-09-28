import os
from time import time as now, sleep
import urllib.request
from prometheus_client import start_http_server, Gauge

#Expects comma-separated URLS as environment variables
# Example: $ URLS=https://google.com/500,https://google.com
urls_from_env = os.getenv('URLS', "")

urls = [url for url in urls_from_env.split(",")]

port = 9100

external_url_up = Gauge('external_url_up', 'Status of external URL', ['url'])
external_url_response_ms = Gauge('external_url_response_ms', 'Response time of external URL in milliseconds', ['url'])

def check_urls(url):
    start_time = now()
    try:
        with urllib.request.urlopen(url, timeout=5) as answer:
            r_code = answer.getcode()
        end_time = now()
        latency  = int((end_time - start_time)*1000)
        is_up    = 1 if r_code == 200 else 0
        # print(f"URL: {url} returned status code: {r_code} for {latency} ms")
    except Exception as e:
        end_time = now()
        latency  = int((end_time - start_time)*1000)
        is_up = 0
        # print(f"URL ERROR")
    external_url_up.labels(url=url).set(is_up)
    external_url_response_ms.labels(url=url).set(latency)

def update_metrics():
    start_http_server(port)
    while True:
        for url in urls:
            check_urls(url)
        sleep(60)

if __name__ == "__main__":
    update_metrics()
