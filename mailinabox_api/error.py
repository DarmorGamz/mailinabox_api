class ApiException(Exception):
    """
    Custom exception class for MailinaBox errors.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"ApiException: {self.message}"
