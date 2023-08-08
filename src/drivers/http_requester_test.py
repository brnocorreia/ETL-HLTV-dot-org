from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    url = 'https://www.vlr.gg/team/6961/loud'
    response_context = '<h1>OlaMundo</h1>'
    requests_mock.get(url, status_code=200, text=response_context)

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()

    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == response_context
    