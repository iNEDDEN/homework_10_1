def filter_by_state(user_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению
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
