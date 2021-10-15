from pyclient.http import PyClient

_SAMPLE_CONFIG = {
    'http': {
        'host': 'https://httpbin.org',
        'port': '',
        'timeouts': {
            'read': 5,
            'connect': 5,
        },
        'retries': {
            'attempts': 3,
            'backoff': 0.5,
            'on_errors': ['500', '502', '504', '429'],
        },
    },
    'basic_auth': {
        'user': 'user',
        'password': 'password',
    },
    'tls': {
        'ca_path': '',  # 'path/to/ca'
        'client_certificate_path': '',  # path/to/client/certificate'
        'client_key_path': '',  # path/to/key'
    },
}

if __name__ == '__main__':
    http_client = PyClient.get_http_client(config=_SAMPLE_CONFIG)
    http_client.do_get(path='/get')
