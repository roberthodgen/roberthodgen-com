from webapp2 import WSGIApplication, Route

from service import handle

ROUTES = [
    Route('/',
          handler=handle.StaticFileHandler),
    Route(r'/<request_uri:[a-z0-9-_/\.]+>',
          handler=handle.StaticFileHandler)
]

APP = WSGIApplication(ROUTES)

