from app.exceptions import InvalidKeyValueError,NotFoundError,InvalidDataError


def check_user(id, model, send_type: str):
    if type(id) != int:
        raise InvalidKeyValueError()

    user = model.query.get(id)

    if not user:
        raise NotFoundError(send_type)

    return user


def check_data(data_received:dict,expected:dict):
    valid_data = {**expected}

    for key,value in expected.items():
        item_received = data_received.get(key)
        if (not item_received):
            raise InvalidDataError(data_received,expected)
        elif(type(item_received) != value):
            raise InvalidDataError(data_received,expected)
        else:
            valid_data[key]= item_received
        
    return valid_data