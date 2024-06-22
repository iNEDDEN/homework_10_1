import masks
from datetime import datetime


def mask_account_card(user_input: str) -> str:
    """Функция, которая делает общую маскировку карты или счета"""
    if "Счет" in user_input:
        user_masked_info = (
                "Счет " + masks.get_mask_account(user_input[5:])
        )
    else:
        card_info = user_input.split()
        card_number = str(card_info[-1])
        user_masked_info = (
                " ".join(card_info[:-1])
                + " " + masks.get_mask_card_number(card_number)
        )
    return user_masked_info


def get_data(user_data_input: str) -> str:
    """Функция, которая преобразовывает дату"""
    new_data = datetime.strptime(
        user_data_input,
        '%Y-%m-%dT%H:%M:%S.%f'
    )
    new_data = datetime.strftime(new_data, '%d.%m.%Y')
    return new_data


if __name__ == "__main__":
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_data("2018-07-11T02:26:18.671407"))
