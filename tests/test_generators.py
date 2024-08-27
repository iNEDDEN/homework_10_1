import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected", [
    ("USD", [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
              'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
              'to': 'Счет 11776614605963066702'},
             {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
              'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
              'to': 'Счет 75651667383060284188'},
             {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
              'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
              'to': 'Visa Platinum 8990922113665229'}]),
    ("EUR", [])
])
def test_filter_by_currency(test_transactions, currency, expected):
    result = list(filter_by_currency(test_transactions, currency))
    assert result == expected


def test_empty_list_filter_by_currency():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_empty_currency_filter_by_currency(test_transactions_empty_currency):
    result = list(filter_by_currency(test_transactions_empty_currency, "USD"))
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        "Отсутствует пункт 'code'",
        "Отсутствует пункт 'code'",
        "Отсутствует пункт 'code'",
        "Отсутствует пункт 'code'"
    ]


@pytest.mark.parametrize("expected", [
    ([
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ])
])
def test_transaction_descriptions(test_transactions, expected):
    result = list(transaction_descriptions(test_transactions))
    assert result == expected


def test_empty_list_transaction_descriptions():
    result = list(transaction_descriptions(([])))
    assert result == []


@pytest.mark.parametrize("start, stop, expected", [
    (0, 3, ["0000 0000 0000 0000",
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
            ]),
    (97, 101, ["0000 0000 0000 0097",
               "0000 0000 0000 0098",
               "0000 0000 0000 0099",
               "0000 0000 0000 0100",
               "0000 0000 0000 0101"
               ]),
    (9999999999999995, 9999999999999999, ["9999 9999 9999 9995",
                                          "9999 9999 9999 9996",
                                          "9999 9999 9999 9997",
                                          "9999 9999 9999 9998",
                                          "9999 9999 9999 9999"
                                          ])
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
