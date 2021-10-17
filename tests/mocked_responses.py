from unittest import mock


def mocked_http_calls(*args, **kwargs):
    response = {"foo": "bar"}
    response_stub = mock.Mock(
        **{
            'json.return_value': response,
            'text': str(response),
            'status_code': 200,
        }
    )

    if args[0] == '/foo':
        return response_stub
