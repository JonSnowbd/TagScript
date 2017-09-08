class TagEngineError(Exception):
    """Unique error for TagEngine"""
    def __init__(self, message):
        self.message = message
        super().__init__()
