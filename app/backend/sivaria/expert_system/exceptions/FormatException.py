from ..exceptions.ApplicationException import ApplicationException

class FormatException(ApplicationException):
    """Exception raised for errors in the input score.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Format exception."):
        self.message = message
        super().__init__(self.message)