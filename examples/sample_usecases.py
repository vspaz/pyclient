from pyclient.http import PyClient
from sample_config import config


if __name__ == "__main__":
    http_client = PyClient.get_http_client(config=config)
