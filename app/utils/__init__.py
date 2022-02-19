from app.exceptions import InvalidKeyValueError,NotFoundError


def check_user(id, model, send_type: str):
    if type(id) != int:
        raise InvalidKeyValueError()

    user = model.query.get(id)

    if not user:
        raise NotFoundError(send_type)

    return user