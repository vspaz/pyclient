from unittest import mock
from .mocked_responses import mocked_http_calls

from pyclient.http import PyClient


def test_client_init_ok():
    _ = PyClient.get_http_client(
        config={
            'http': {
                'host': 'http://example.com',
            },
        }
    )


@mock.patch('pyclient.http.PyClient.do_get', side_effect=mocked_http_calls)
def test_client_get_ok(mock_get):
    http_client = PyClient.get_http_client(
        config={
            'http': {
                'host': 'http://example.com',
            },
        }
    )
    resp = http_client.do_get("/foo")
    assert resp.json() == {"foo": "bar"}
    assert resp.status_code == 200
