import logging


class ClassA(object):
    def __init__(self, name, logger=None, **kwargs):
        self.logger = logger or logging.getLogger(__name__)
        self.name = kwargs.get('name', None)

    def my_method(self):
        self.logger.info('calling my_method')
