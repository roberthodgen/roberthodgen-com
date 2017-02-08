from webapp2 import WSGIApplication, Route

from service import handle


ROUTES = [
    Route('/_ah/warmup',
          handler=handle.StatusHandler),
    Route('/api/v1/status',
          handler=handle.StatusHandler)
]

APP = WSGIApplication(ROUTES)
APP.error_handlers[405] = handle.http_error
