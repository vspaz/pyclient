from jsonschema import Draft4Validator, validate


def _validate_config(config, schema):
    validate(instance=config, schema=schema, cls=Draft4Validator)
