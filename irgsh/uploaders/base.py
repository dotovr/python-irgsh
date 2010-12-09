import logging

class UploadFailedError(Exception):
    pass

class BaseUploader(object):
    def __init__(self, distribution, **opts):
        self.distribution = distribution

        self.log = logging.getLogger('irgsh.uploaders')

    def upload(self, changes, stdout=None, stderr=None):
        raise NotImplementedError()

