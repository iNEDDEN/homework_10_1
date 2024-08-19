import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize("input_data, expected", [
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Classic 683198247673765", "Номер карты должен содержать 16 цифр!"),
    ("Visa Classic 68319824767376588", "Номер карты должен содержать 16 цифр!"),
    ("Visa Classic", "Номер карты должен содержать 16 цифр!"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 6468647367889477958999", "Номер счета должен содержать 20 цифр!"),
    ("Счет 646864736788", "Номер счета должен содержать 20 цифр!"),
    ("Счет", "Номер счета должен содержать 20 цифр!")
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2018-70-11T02:26:18.671407", "Неправильный формат даты"),
    ("20188-07-11T02:26:18.671407", "Неправильный формат даты"),
    ("", "Неправильный формат даты")
])
def test_get_data(input_data, expected):
    assert get_data(input_data) == expected
