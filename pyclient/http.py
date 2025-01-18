from __future__ import annotations

from typing import Union

import requests
import ujson
from urllib3.util.retry import Retry

from .__version__ import __version__
from .logger import log_request

requests.models.complexjson = ujson


class PyClient:
    def __init__(self, host: str = "", port: Union[str, int] = "") -> None:
        self._session: requests.Session = requests.Session()
        self._host: str = f"{host}{':' + str(port) if port else ''}"
        self._timeouts: tuple[float, float] = (5, 5)
        self.set_retries()
        self.set_user_agent()

    @log_request
    def _request(
            self, url: str, method: str,
            **kwargs: dict,
    ) -> requests.Response:
        return self._session.request(
            method=method,
            url=url,
            timeout=kwargs.get("timeouts", self._timeouts),
            **kwargs,
        )

    def request(self, path: str, method="GET", **kwargs) -> requests.Response:
        return self._request(url=self._host + path, method=method, **kwargs)

    def do_get(self, path: str, **kwargs) -> requests.Response:
        return self.request(path=path, **kwargs)

    def do_post(self, path: str, **kwargs) -> requests.Response:
        return self.request(path=path, method="POST", **kwargs)

    def do_patch(self, path: str, **kwargs) -> requests.Response:
        return self.request(path=path, method="PATCH", **kwargs)

    def do_delete(self, path: str, **kwargs) -> requests.Response:
        return self.request(path=path, method="DELETE", **kwargs)

    def do_put(self, path: str, **kwargs) -> requests.Response:
        return self.request(path=path, method="PUT", **kwargs)

    def do_head(self, path: str, **kwargs) -> requests.Response:
        return self.request(path=path, method="HEAD", **kwargs)

    def set_tls(self, client_certificate_path, client_key_path, ca_path=None) -> None:
        self._session.cert = (client_certificate_path, client_key_path)
        self._session.verify = ca_path

    def set_basic_auth(self, user, password) -> None:
        self._session.auth = (user, password)

    @staticmethod
    def _retry_on(count: int, backoff: Union[int, float], on_errors: list) -> requests.adapters.HTTPAdapter:
        return requests.adapters.HTTPAdapter(
            max_retries=Retry(
                total=count,
                backoff_factor=backoff,
                status_forcelist=on_errors or [],
            ),
        )

    def set_retries(self, count=0, backoff=0, on_errors=None) -> None:
        self._session.mount(
            prefix=self._host or "https://",
            adapter=self._retry_on(count=count, backoff=backoff, on_errors=on_errors),
        )

    def set_user_agent(self, ua=None) -> None:
        self._session.headers = {"user-agent": ua or f'PyClient/{__version__}'}

    def set_timeouts(self, connect: int = 5, read: int = 5) -> None:
        self._timeouts: tuple = (connect, read)

    @staticmethod
    def get_http_client(host: str = "", port: Union[int, str] = "") -> PyClient:
        return PyClient(host=host, port=port)
