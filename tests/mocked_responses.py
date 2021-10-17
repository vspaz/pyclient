from unittest import mock


def _response_factory(path: str):
    path_to_response = {
        '/get': {
            'json.return_value': {"foo": "bar"},
            'text': str({"foo": "bar"}),
            'status_code': 200,
        },
        '/post': {
            'json.return_value': {"status": "accepted"},
            'text': str({"status": "accepted"}),
            'status_code': 202,
        },
        '/patch': {
            'json.return_value': {"status": "accepted"},
            'text': str({"status": "accepted"}),
            'status_code': 202,
        },
    }
    mocked_response = path_to_response.get(path)
    assert mocked_response, 'response not yet defined'
    return mock.Mock(**mocked_response)


def mocked_http_calls(*args, **kwargs):
    return _response_factory(path=args[0])
