import requests
import ujson
from urllib3.util.retry import Retry

requests.models.complexjson = ujson


class PyClient:
    def __init__(self, config: dict):
        # TODO: add validation.
        self._session: requests.Session = requests.Session()
        http_config = config['http']
        port = str(http_config.get('port', ''))

        self._session.mount(
            prefix=f"{http_config['host']}" + f":{port}/" if port else '/',
            adapter=self._retry_on(config=http_config.get('retries', {})),
        )
        tls_certificates = config.get('tls', {})
        if tls_certificates:
            self._session.verify = tls_certificates['ca_path']
            self._session.cert = (
                tls_certificates['client_certificate_path'],
                tls_certificates['client_key_path'],
            )

    @staticmethod
    def _retry_on(config: dict):
        return requests.adapters.HTTPAdapter(
            max_retires=Retry(
                total=config.get('retries', 3),
                backoff_factor=config.get('backoff', 0.5),
                status_forcelist=config.get('on_errors', []),
            ),
        )

    def _request(self, url, method, **kwargs):
        return self._session.request(
            method=method,
            url=url,
            timeout=kwargs.get('timeouts', (5, 5)),
            **kwargs,
        )

    @staticmethod
    def _validate_config():
        pass

    @staticmethod
    def get_http_client(config: dict):
        return PyClient(config=config)
