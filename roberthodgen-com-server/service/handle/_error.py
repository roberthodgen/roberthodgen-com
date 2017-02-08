class HandlerError(Exception):
    description = 'Internal Server Error'
    _default_reason = 'Unexpected server error prevented req fulfillment.'

    def __init__(self, reason=_default_reason, code=500):
        super(HandlerError, self).__init__()
        self.reason = reason
        self.code = code
        self.headers = dict()


class BadRequestError(HandlerError):
    description = 'Bad Request'
    _default_reason = 'Request could not be understood.'

    def __init__(self, reason=_default_reason):
        super(BadRequestError, self).__init__(reason, code=400)


class UnauthorizedError(HandlerError):
    description = 'Unauthorized'
    _default_reason = 'This resource requires authentication.'

    def __init__(self, reason=_default_reason):
        super(UnauthorizedError, self).__init__(reason, code=401)
        self.headers.update({
            'www-authenticate': 'Bearer'
        })


class NotFoundError(HandlerError):
    description = 'Not Found'
    _default_reason = 'Found nothing this resource URI.'

    def __init__(self, reason=_default_reason):
        super(NotFoundError, self).__init__(reason, code=404)


class MethodNotAllowedError(HandlerError):
    description = 'Method Not Allowed'
    _default_reason = 'Method not allowed for this resource URI.'

    def __init__(self, reason=_default_reason, allow=None):
        super(MethodNotAllowedError, self).__init__(reason, code=405)
        if isinstance(allow, list):
            self.headers.update(allow=', '.join(allow))
