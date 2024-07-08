def filter_by_state(user_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    filtered_list = list()
    for i in range(len(user_list)):
        if user_list[i]["state"] == state:
            filtered_list.append(user_list[i])
    return filtered_list


def sort_by_date(user_list: list, sort_filter: bool = True) -> list:
    """
    Функция, которая возвращает новый список, отсортированный по дате
    """
    sorted_list_date = sorted(user_list,
                              key=lambda x: x["date"],
                              reverse=sort_filter)
    return sorted_list_date


if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                          ))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                       ))
