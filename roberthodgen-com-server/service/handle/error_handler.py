from webapp2 import HTTPException

from _error import HandlerError

import json

import logging


def http_error(_, response, exception):
    """
    Error Handler for webapp2 Route handlers.
    :param _: Unused req object
    :param response:
    :param exception:
    :return:
    """
    logging.exception(exception)
    if isinstance(exception, HandlerError):
        return _HandlerErrorWorker(response, exception).work()
    if isinstance(exception, HTTPException):
        return _HTTPExceptionWorker(response, exception).work()
    if isinstance(exception, Exception):
        return _Worker(response, exception).work()
    return exception


class _Worker(object):
    def __init__(self, response, exception):
        self.response = response
        self.exception = exception

    def work(self):
        self.response.set_status(500)
        self.response.content_type = 'application/json'
        self.response.out.write(self.get_json())
        return self.response

    def get_json(self):
        o = dict()
        o['description'] = 'Internal Server Error'
        o['reason'] = str(self.exception)
        o['code'] = 500
        return json.dumps(o)


class _HandlerErrorWorker(_Worker):
    def work(self):
        self.response.set_status(self.exception.code)
        self.response.content_type = 'application/json'
        self.add_headers()
        self.response.out.write(json.dumps(self.get_json()))
        return self.response

    def get_json(self):
        o = dict()
        o['description'] = self.exception.description
        o['reason'] = self.exception.reason
        o['code'] = self.exception.code
        return json.dumps(o)

    def add_headers(self):
        for header in self.exception.headers:
            self.response.headers.add(header, self.exception.headers.get(header))


class _HTTPExceptionWorker(_Worker):
    def work(self):
        self.response.set_status(self.exception.code)
        self.response.set_content_type = 'application/json'
        self.response.out.write(json.dumps(self.get_json()))
        return self.response

    def get_json(self):
        o = dict()
        o['description'] = self.exception.title
        o['reason'] = str(self.exception)
        o['code'] = self.exception.code
        return json.dumps(o)
