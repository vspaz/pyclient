from unittest import mock


def _response_factory(path: str):
    common_mock_response = {
        'json.return_value': {'status': 'accepted'},
        'text': str({'status': 'accepted'}),
        'status_code': 202,
    }

    get_response = {
        'json.return_value': {'foo': 'bar'},
        'text': str({'foo': 'bar'}),
        'status_code': 200,
    }

    path_to_response = {
        '/get': get_response,
        'http://example.com/get': get_response,
        '/post': common_mock_response,
        '/patch': common_mock_response,
        '/put': common_mock_response,
        '/delete': common_mock_response,
    }
    mocked_response = path_to_response.get(path)
    assert mocked_response, 'response not yet defined'
    return mock.Mock(**mocked_response)


def mocked_http_calls(*args, **kwargs):
    return _response_factory(path=args[0])
