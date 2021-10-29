# pyclient

configurable HTTP python client that supports

- tls,
- basic auth,
- retries on specific errors,
- timeouts,
- logging
- uses ultra-fast 'ujson' library for serialization'
- etc.

the config is optional.
below is the config sample:

```python
from pyclient.http import PyClient

config = {
    'http': {
        'host': 'https://httpbin.org',
        'port': '',  # <int|str>
        'timeouts': {
            'read': 5,
            'connect': 5,
        },
        'retries': {
            'attempts': 3,
            'backoff': 0.5,
            'on_errors': [500, 502, 504, 429, ],
        },
    },
    'basic_auth': {
        'user': 'user',
        'password': 'password',
    },
    'tls': {
        'ca_path': 'path/to/ca',
        'client_certificate_path': 'path/to/client/certificate',
        'client_key_path': 'path/to/key',
    }
}

http_client = PyClient.get_http_client(config=config)
resp = http_client.do_get(path='/get')  # -> https://httpbin.org/get

```
w/o config
```python
from pyclient.http import PyClient


http_client = PyClient.get_http_client()
resp = http_client.do_get(path="https://httpbin.org/get")
```
