class NotFoundError(Exception):
    def __init__(self, send_type: str) -> None:
        self.message = {
            "message": f"{send_type} not found"
        }
        super().__init__(self.message)


class InvalidIdValueError(Exception):
    def __init__(self) -> None:
        self.message = {
            "message": "id must be an integer"
        }
        super().__init__(self.message)

class InvalidDataError(Exception):
    data_types = {
        str:"string",
        int:"integer",
        float:"float",
        list:"list",
        bool:"boolean"
    }
    def __init__(self,data_received:dict,expected_data:dict):
        self.message = {
            "expected":{key:self.data_types[value] for key,value in expected_data.items()},
            "received":{key: self.data_types[type(value)] for key,value in data_received.items()}
        }
        super().__init__(self.message)