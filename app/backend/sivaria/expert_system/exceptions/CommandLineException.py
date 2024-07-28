from ..exceptions.ApplicationException import ApplicationException

class CommandLineException(ApplicationException):
    """Exception raised for errors in the input command line.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Error in the command line arguments."):
        self.message = message
        super().__init__(self.message)