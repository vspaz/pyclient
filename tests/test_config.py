import jsonschema
import pytest

from pyclient import schemas


def test_host_present_ok():
    config = {
        'http': {
            'host': 'http://example.com'
        }
    }

    schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)


def test_host_missing_fail():
    config = {
        'http': {

        }
    }

    with pytest.raises(jsonschema.ValidationError):
        schemas._validate_config(config=config, schema=schemas.CONFIG_SCHEMA)


def test_config_empty_fail():
    with pytest.raises(jsonschema.ValidationError):
        schemas._validate_config(config=dict(), schema=schemas.CONFIG_SCHEMA)
