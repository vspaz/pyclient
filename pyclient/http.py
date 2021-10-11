import requests
import ujson

from urllib3.util.retry import Retry

requests.models.complexjson = ujson


class PyClient:
    def __init__(self, config: dict):
        self._session: requests.Session = requests.Session()
        self._session.mount("https://", self._retry_on(config=config))
        self._session.mount("http://", self._retry_on(config=config))

    @staticmethod
    def _retry_on(config: dict):
        return requests.adapters.HTTPAdapter(
            max_retires=Retry(
                total=config.get("retries", 3),
                backoff_factor=config.get("backoff", 0.5),
                status_forcelist=config.get("on_errors", []),
            )
        )

    def _request(self, url, method, **kwargs):
        return self._session.request(
            method=method,
            url=url,
            timeout=kwargs.get("timeouts", (5, 5)),
            **kwargs,
        )

    @staticmethod
    def get_http_client(config: dict):
        return PyClient(config=config)
