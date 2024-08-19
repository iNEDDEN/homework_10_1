from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция, которая делает общую маскировку карты или счета"""
    if "Счет" in user_input:
        if len(user_input[5:]) != 20:
            return "Номер счета должен содержать 20 цифр!"
        user_masked_info = "Счет " + get_mask_account(user_input[5:])
    else:
        card_info = user_input.split()
        card_number = str(card_info[-1])
        if len(card_number) != 16:
            return "Номер карты должен содержать 16 цифр!"
        user_masked_info = (" ".join(card_info[:-1])
                            + " " + get_mask_card_number(card_number))
    return user_masked_info


def get_data(user_data_input: str) -> str:
    """Функция, которая преобразовывает дату"""
    try:
        new_data_datetime = datetime.strptime(
            user_data_input,
            "%Y-%m-%dT%H:%M:%S.%f"
        )
    except ValueError:
        return "Неправильный формат даты"
    new_data = datetime.strftime(new_data_datetime, "%d.%m.%Y")
    return new_data
