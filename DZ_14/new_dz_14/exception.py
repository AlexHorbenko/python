__all__ = ('UserException',)

class UserException(Exception):
    def __init__(self, message):
        self.message = message

    def get_exception_message(self):
        return self.message