def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")

    if " " in password:
        raise ValueError("Пароль не должен содержать пробелы")

    if not (8 <= len(password) <= 20):
        return False
    if not any(ch.isupper() for ch in password):
        return False
    if not any(ch.islower() for ch in password):
        return False
    if not any(ch.isdigit() for ch in password):
        return False

    special = "!@#$%^&*"
    if not any(ch in special for ch in password):
        return False

    return True
    """
    :param password: Проверяемый пароль
    :return: True, если пароль удовлетворяет всем условиям, иначе False
    :raises TypeError: Если входной параметр не является строкой
    :raises Val
    """