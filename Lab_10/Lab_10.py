import pytest


class HttpRequest:
    def __init__(self, line):
        x = line.split(' ')
        self.request = x[0]
        self.path = x[1]
        self.protocol = x[2]

        if self.request not in ["GET", "POST", "HEAD", "PUT", "DELETE", "TRACE", "OPTIONS", "CONNECT", "PATCH"]:
                raise Bad_Request_Type_Error

        if self.protocol not in ["HTTP/1.0", "HTTP/1.1", "HTTP/2.0"]:
            raise BadHTTPVersion


        if "/" not in self.path:
            raise ValueError



    def __str__(self):
        return f'Request type: {self.request} Resource: {self.protocol} Path: {self.path}'

    def return_method(self):
        return self.request

    def return_resource(self):
        return self.protocol

    def return_path(self):
        return self.path


def reqstr2obj(request_string):
    if type(request_string) != str:
        raise type_error
    else:
        my_split = request_string.split(' ')
        if len(my_split) == 3:
            return HttpRequest(request_string)
            #pass
        else:
            raise value_error


class type_error(TypeError):
    pass


class value_error(ValueError):
    pass


class Bad_Request_Type_Error(Exception):
    pass


class BadHTTPVersion(Exception):
    pass


def test_reqstr2obj():
    with pytest.raises(type_error):
        reqstr2obj(0)


my_argument = "GET / HTTP/1.1"


def test_reqstr2obj2():
    assert type(reqstr2obj(my_argument)) == HttpRequest


def test_reqstr2obj3():
    x = HttpRequest(my_argument)
    assert x.request == 'GET'
    assert x.path == '/'
    assert x.protocol == 'HTTP/1.1'


def test_reqstr2obj4():#problem
    my_request = 'HEAD /test HTTP/1.0'
    test = reqstr2obj(my_request)
    assert test.request == (my_request.split(' '))[0] \
        and test.path == (my_request.split(' '))[1] \
        and test.protocol == (my_request.split(' '))[2]


def test_reqstr2obj5():
    with pytest.raises(value_error):
        reqstr2obj(my_argument + " test")


def test_reqstr2obj6():
    with pytest.raises(Bad_Request_Type_Error):
        reqstr2obj("DOWNLOAD /movie.mp4 HTTP1.1")


def test_reqstr2obj7():
    with pytest.raises(BadHTTPVersion):
        reqstr2obj('GET / HTTP/1.9')


def test_reqstr2obj8():
    with pytest.raises(ValueError):
        reqstr2obj('GET \ HTTP/1.0')





