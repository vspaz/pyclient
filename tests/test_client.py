from unittest import mock

from pyclient.http import PyClient
from .mocked_responses import mocked_http_calls


def test_client_init_ok():
    _ = PyClient.get_http_client(
        config={
            'http': {
                'host': 'http://example.com',
            },
        },
    )


@mock.patch('pyclient.http.PyClient.do_get', side_effect=mocked_http_calls)
def test_do_get_ok(mock_do_get):
    http_client = PyClient.get_http_client(
        config={
            'http': {
                'host': 'http://example.com',
            },
        },
    )
    resp = http_client.do_get('/get')
    assert resp.text == "{'foo': 'bar'}"
    assert resp.status_code == 200
    assert resp.json() == {'foo': 'bar'}


@mock.patch('pyclient.http.PyClient.do_post', side_effect=mocked_http_calls)
def test_do_post_ok(mock_do_post):
    http_client = PyClient.get_http_client(
        config={
            'http': {
                'host': 'http://example.com',
            },
        },
    )
    resp = http_client.do_post('/post', json={'foo', 'bar'})
    assert resp.text == "{'status': 'accepted'}"
    assert resp.status_code == 202
    assert resp.json() == {'status': 'accepted'}


@mock.patch('pyclient.http.PyClient.do_patch', side_effect=mocked_http_calls)
def test_do_patch_ok(mock_do_patch):
    http_client = PyClient.get_http_client(
        config={
            'http': {
                'host': 'http://example.com',
            },
        },
    )
    resp = http_client.do_patch('/patch', json={'foo': 'bar'})
    assert resp.text == "{'status': 'accepted'}"
    assert resp.status_code == 202
    assert resp.json() == {'status': 'accepted'}
