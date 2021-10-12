from pyclient import http
from sample_config import config

if __name__ == "__main__":
    http_client = http.PyClient.get_http_client(config=config)
