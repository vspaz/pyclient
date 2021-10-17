def mocked_http_calls(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def status_code(self):
            return self.status_code

    if args[0] == '/foo':
        return MockResponse({"foo": "bar"}, 200)

    return MockResponse(args, 404)
