def get_mask_card_number(user_input: int) -> str:
    """Функция, которая маскирует номер карты"""
    new_list = []
    new_str = str(user_input)[:6] + "******" + str(user_input)[-4:]
    for i in range(0, len(new_str), 4):
        new_list.append(new_str[i : i + 4])
    return " ".join(new_list)


def get_mask_account(user_input: int) -> str:
    """Функция, которая маскирует номер счета"""
    return "**" + str(user_input)[-4:]


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
