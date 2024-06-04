from exceptions.ApplicationException import ApplicationException

class ClassifierNotFoundException(ApplicationException):
    """Exception raised for errors in the input classifier.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Given classifier not found."):
        self.message = message
        super().__init__(self.message)