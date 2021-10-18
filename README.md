# pyclient

configurable HTTP python client that supports

- tls,
- basic auth,
- retries on specific errors,
- timeouts,
- logging
- uses ultra-fast 'ujson' library for serialization'
- etc.

sample config

```python
from pyclient.http import PyClient

config = {
    'http': {
        'host': 'https://example.com',  # required
        'port': '',  # optional <int|str>
        # optional section
        'timeouts': {
            'read': 5,
            'connect': 5,
        },
        # optional section
        'retries': {
            'attempts': 3,
            'backoff': 0.5,
            'on_errors': [500, 502, 504, 429, ],
            # optional, errors to retry on
        },
    },
    # optional section
    'basic_auth': {
        'user': 'user',
        'password': 'password',
    },
    # optional section
    'tls': {
        'ca_path': 'path/to/ca',
        'client_certificate_path': 'path/to/client/certificate',
        'client_key_path': 'path/to/key',
    }
}

http_client = PyClient.get_http_client(config=config)
resp = http_client.do_get(path='/movies')  # -> https://example.com/movies
```
