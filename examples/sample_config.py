config = {
    "http": {
        "timeouts": {
            "read": 5,
            "connect": 5,
        },
        "retries": {
            "attempts": 3,
            "backoff": 0.5,
            "on_errors": [],
        }
    },
    "basic_auth": {
        "user": "user",
        "password": "password",
    },
    "tls": {
        "ca_path": "path/to/ca",
        "client_certificate_path": "path/to/client/certificate",
        "client_key_path": "path/to/key",
    },
    "user_agent": "",
}
