def filter_by_state(state_list: list, state="EXECUTED") -> list:
    '''Функция принимает список словарей и опционально значение для ключа state
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению'''
    new_state_list = list()
    for item in state_list:
        if item.get("state") == state:
            new_state_list.append(item)
    return new_state_list


def sort_by_date(dict_list: list, reverse=True) -> list:
    '''Функция принимает список словарей и сортирует их по дате.
    По умолчанию сортировка на убывание'''
    return sorted(dict_list, key=lambda x: x["date"], reverse=reverse)
