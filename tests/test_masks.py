import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("input_data, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("a000792289606361", "Номер карты должен содержать 16 цифр!"),
    ("", "Номер карты должен содержать 16 цифр!"),
    ("700079228960636", "Номер карты должен содержать 16 цифр!"),
    ("70007922896063611", "Номер карты должен содержать 16 цифр!")
])
def test_get_mask_card_number(input_data, expected):
    assert get_mask_card_number(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    ("73654108430135874305", "**4305"),
    ("a3654108430135874305", "Номер счета должен содержать 20 цифр!"),
    ("", "Номер счета должен содержать 20 цифр!"),
    ("7365410843013587430", "Номер счета должен содержать 20 цифр!"),
    ("736541084301358743051", "Номер счета должен содержать 20 цифр!")
])
def test_get_mask_account(input_data, expected):
    assert get_mask_account(input_data) == expected
