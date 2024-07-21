from ..exceptions.ApplicationException import ApplicationException

class PredictionErrorException(ApplicationException):
    """Exception raised for errors in the application.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Error in the application."):
        self.message = message
        super().__init__(self.message)