import os

from _abstract_handler import AbstractHandler

STATIC_DIR = os.path.abspath('dist')

STATIC_FILES = os.listdir(STATIC_DIR)

CONTENT_TYPE_MAP = {
    'html': 'text/html',
    'js': 'application/javascript',
    'css': 'text/css',
    'jpg': 'image/jpeg',
    'png': 'image/png'
}


class StaticFileHandler(AbstractHandler):
    allowed_methods = ['GET']

    def process(self, *args, **kwargs):
        request_uri = kwargs.get('request_uri')
        if request_uri in STATIC_FILES:
            return FileReader(None, STATIC_DIR, request_uri).read()
        return FileReader(None, STATIC_DIR, 'app.html').read()


class FileReader(object):
    def __init__(self, cache, path, filename):
        self.cache = cache
        self.path = path
        self.filename = filename

    def read(self):
        content_type = self.get_content_type()
        content = self.read_contents()
        return content_type, content

    def get_content_type(self):
        content_type = CONTENT_TYPE_MAP.get(self.filename.split('.')[-1])
        if content_type is None:
            return 'text/plain'
        return content_type

    def read_contents(self):
        content = []
        with open(os.path.join(self.path, self.filename)) as f:
            for line in f:
                content.append(line)
        return ''.join(content)
