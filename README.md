# pclient

configurable HTTP python client that supports

- retries on errors,
- timeouts,
- tls,
- basic auth,
- logging etc.

sample config

```python
config = {
    'http': {
        'host': 'https://example.com',  # required
        'port': '',  # optional <int|str> 
        # optional section
        'timeouts': {  
            'read': 5,
            'connect': 5,
        },
        'retries': {  # optional section
            'attempts': 3,
            'backoff': 0.5,
            'on_errors': ['500', '502', '504', '429'],   # optional, errors to retry on 
        },
    },
    'basic_auth': {  # optional
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
```