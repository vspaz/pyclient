from pyclient.http import PyClient

if __name__ == '__main__':
    http_client = PyClient.get_http_client(host='https://httpbin.org')
    http_client.set_retries(count=3, backoff=1.5, on_errors=[500, 502, 504, 429])
    http_client.set_timeouts(connect=5, read=5)
    http_client.set_user_agent(ua='myClient')
    http_client.set_basic_auth(user='user', password='password')
    # http_client.set_tls(
    #     client_key_path='path/to/key',
    #     client_certificate_path='path/to/client/certificate',
    #     ca_path='path/to/ca',
    # )
    print(http_client.do_get(path='/get').json())

    # or simply
    http_client = PyClient.get_http_client()
    print(http_client.do_get(path='https://httpbin.org/get').json())
