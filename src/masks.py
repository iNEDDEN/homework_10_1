def get_mask_card_number(user_input: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(user_input) != 16 or user_input.isdigit() is False:
        return "Номер карты должен содержать 16 цифр!"
    new_list = []
    new_str = user_input[:6] + "******" + user_input[-4:]
    for i in range(0, len(new_str), 4):
        new_list.append(new_str[i: i + 4])
    return " ".join(new_list)


def get_mask_account(user_input: str) -> str:
    """Функция, которая маскирует номер счета"""
    if len(user_input) != 20 or user_input.isdigit() is False:
        return "Номер счета должен содержать 20 цифр!"
    return "**" + user_input[-4:]
