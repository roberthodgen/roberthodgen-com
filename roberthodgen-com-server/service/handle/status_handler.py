from _abstract_handler import AbstractHandler


class StatusHandler(AbstractHandler):
    allowed_methods = ['GET']

    def process(self, *args, **kwargs):
        return dict(success=True)
