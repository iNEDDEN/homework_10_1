def filter_by_currency(user_list_dict, user_currency):
    """Генератор, который поочередно выдает транзакции, где валюта соответствует заданной"""
    for transaction in user_list_dict:
        try:
            if transaction["operationAmount"]["currency"]["code"] == user_currency:
                yield transaction
        except KeyError:
            yield "Отсутствует пункт 'code'"


def transaction_descriptions(user_list_dict):
    """Генератор, который возвращает описание каждой операции по очереди"""
    for transaction in user_list_dict:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number_card in range(start, stop + 1):
        sample_card = ""
        while len(sample_card) + len(str(number_card)) < 16:
            sample_card += "0"
        full_card_number = list(sample_card + str(number_card))
        for index in range(4, len(full_card_number), 5):
            full_card_number.insert(index, " ")
        full_card_number = "".join(full_card_number)
        yield full_card_number
