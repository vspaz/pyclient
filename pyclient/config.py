import functools

from jsonschema import Draft4Validator, validate


def _validate_config(config, schema):
    validate(instance=config, schema=schema, cls=Draft4Validator)


def validate_config(schema):
    def _wrapper(func):
        @functools.wraps(func)
        def __wrapper(*args, **kwargs):
            _validate_config(config=kwargs['config'], schema=schema)
            return func(*args, **kwargs)

        return __wrapper

    return _wrapper


_TIMEOUTS = {
    'type': 'object',
    'properties': {
        'connect': {
            'type': 'number',
        },
        'read': {
            'type', 'number',
        },
    }
}

_HTTP = {
    'type': 'object',
    'properties': {
        'host': {
            'type': 'string',
        },
        'port': {
            'type': ['number', 'string', ]
        },
        'timeouts': _TIMEOUTS,
    },
    'required': ['host', ],
    'additionalProperties': False
}

_BASIC_AUTH = {
    'type': 'object',
    'properties': {
        'user': {
            'type': 'string',
        },
        'password': {
            'type': 'string',
        },
    }
}

_TLS = {
    'type': 'object',
    'properties': {
        'ca_path': {
            'type': 'string',
        },
        'client_certificate_path': {
            'type': 'string',
        },
        'client_key_path': {
            'type': 'string',
        },
    }
}

CONFIG_SCHEMA = {
    'type': 'object',
    'properties': {
        'http': _HTTP,
        'basic_auth': _BASIC_AUTH,
        'tls': _TLS,
    },
    'required': ['http', ],
    'additionalProperties': False,
}
