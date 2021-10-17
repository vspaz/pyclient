import jsonschema
import pytest

from pyclient import schemas


def test_host_present_ok():
    config = {
        'http': {
            'host': 'http://example.com',
        },
    }

    schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)


def test_host_missing_fail():
    config = {
        'http': {

        },
    }

    with pytest.raises(jsonschema.ValidationError):
        schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)


def test_empty_config_fail():
    with pytest.raises(jsonschema.ValidationError):
        schemas._validate_config(config=dict(), schema=schemas.CONFIG_SCHEMA)


def test_extra_fields_fail():
    config = {
        'http': {
            'host': 'http: // example.com',
            'some_extra_field': "extra field value",
        },
    }

    with pytest.raises(jsonschema.ValidationError):
        schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)


def test_full_config_ok():
    config = {
        'http': {
            'host': '',
            'port': '',
            'timeouts': {
                'read': 5,
                'connect': 5,
            },
            'retries': {
                'attempts': 3,
                'backoff': 0.5,
                'on_errors': [500, 502, 504, 429],
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
        },
    }

    schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)
