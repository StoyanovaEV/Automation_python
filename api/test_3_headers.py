import re
from api.httpbin_api import http_bin_api
from http import HTTPStatus

def test_list_html():
    res = http_bin_api.list_html()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/html; charset=utf-8'

    assert re.fullmatch(r'^<!DOCTYPE html>.+', res.text, flags=re.DOTALL)

def test_robots():
    res = http_bin_api.robots_txt()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', res.text, flags=re.DOTALL
                    )






