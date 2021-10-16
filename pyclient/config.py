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
