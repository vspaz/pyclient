import pytest
from pyclient import schemas


def test_host_present_ok():
    config = {
        'http': {
            'host': 'http://example.com'
        }
    }

    schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)
