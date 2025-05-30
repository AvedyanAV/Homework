def get_date(date_str: str) -> str:
    """Функция возвращает отфильтрованную дату"""
    if len(date_str) <= 0:
        return "Некорректный формат даты"
    date_part = str(date_str.split("T")[0])
    year, month, day = date_part.split("-")
    if int(year) <= 0000 or int(month) <= 0 or int(day) <= 0:
        return "Некорректный формат даты"
    elif int(year) > 9999 or int(month) > 12 or int(day) > 31:
        return "Некорректный формат даты"
    elif int(month) == 2 and int(day) > 28:
        return "Некорректный формат даты"
    elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11 and int(day) > 30:
        return "Некорректный формат даты"
    return f"{day}.{month}.{year}"


def mask_account_card(card_number: str) -> str:
    """Функция возвращает номер счета и карты со скрытыми символами"""
    if 'счет' in card_number.lower():
        parts = card_number.split()

        account_type = ' '.join(parts[:-1])
        account_number = parts[-1]

        from src.masks import get_mask_account
        masked_number = get_mask_account(int(account_number))
        return f"{account_type} {masked_number}"
    else:
        parts = card_number.split()

        card_type = ' '.join(parts[:-1])
        card_number = parts[-1]

        from src.masks import get_mask_card_number
        masked_number = get_mask_card_number(int(card_number))
        return f"{card_type} {masked_number}"
