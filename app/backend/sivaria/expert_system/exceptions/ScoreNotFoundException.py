from ..exceptions.ApplicationException import ApplicationException

class ScoreNotFoundException(ApplicationException):
    """Exception raised for errors in the input score.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Given score not found."):
        self.message = message
        super().__init__(self.message)