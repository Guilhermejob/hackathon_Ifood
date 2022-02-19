class NotFoundError(Exception):
    def __init__(self, send_type: str) -> None:
        self.message = {
            "message": f"{send_type} not found"
        }
        super().__init__(self.message)


class InvalidKeyValueError(Exception):
    def __init__(self) -> None:
        self.message = {
            "message": "id must be an integer"
        }
        super().__init__(self.message)