from webapp2 import RequestHandler

import json

from _error import MethodNotAllowedError, HandlerError

from error_handler import http_error


class AbstractHandler(RequestHandler):
    allowed_methods = []

    def handle_exception(self, exception, debug):
        """
        Handle an uncaught exception from within an Handler.
        :param exception: The raised exception.
        :param debug: WSGIApplication debug
        :return: None
        """
        http_error(self.request, self.response, exception)

    def pre_process(self):
        pass

    def post_process(self):
        pass

    def process(self, method, *args, **kwargs):
        """
        Process work for the Handler. Should be overridden by subclasses.
        :param method: HTTP Request Method
        :param args:
        :param kwargs:
        """
        raise HandlerError()

    def _validate_method(self, method):
        """
        Validates this Handler can process a given HTTP Request Method.
        :param method: HTTP Request Method
        :return: None
        """
        if method not in self.allowed_methods:
            raise MethodNotAllowedError(allow=self.allowed_methods)

    def _process(self, *args, **kwargs):
        """
        Executes validations, handler processing, pre and post processors, response handling.
        :param args:
        :param kwargs:
        :return: Response
        """
        self._validate_method(*args)
        self.pre_process()
        response = self.process(*args, **kwargs)
        self.post_process()
        if isinstance(response, dict) or isinstance(response, list):
            return self.respond_json(response)
        if isinstance(response, tuple):
            return self.respond_with_content_type(*response)
        if isinstance(response, basestring):
            return self.respond_text(response)

    def respond_json(self, obj):
        """
        Write :param obj: to the response as a JSON-encoded string.
        :param obj:
        :return: Response
        """
        self.response.content_type = 'application/json'
        self.response.out.write(json.dumps(obj))
        return self.response

    def respond_with_content_type(self, content_type, content):
        if content_type is not None:
            self.response.content_type = content_type
        self.response.out.write(content)
        return self.response

    def respond_text(self, text):
        """
        Write :param text: to the response as text.
        :param text:
        :return: Response
        """
        self.response.out.write(text)
        return self.response

    def get(self, *args, **kwargs):
        """
        HTTP GET req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('GET', *args, **kwargs)

    def put(self, *args, **kwargs):
        """
        HTTP PUT req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('PUT', *args, **kwargs)

    def post(self, *args, **kwargs):
        """
        HTTP POST req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('POST', *args, **kwargs)

    def head(self, *args, **kwargs):
        """
        HTTP HEAD req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('HEAD', *args, **kwargs)

    def options(self, *args, **kwargs):
        """
        HTTP OPTIONS req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('OPTIONS', *args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        HTTP DELETE req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('DELETE', *args, **kwargs)

    def trace(self, *args, **kwargs):
        """
        HTTP TRACE req.
        :param args:
        :param kwargs:
        :return: Response
        """
        return self._process('TRACE', *args, **kwargs)
