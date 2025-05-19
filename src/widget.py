def get_date(date_str: str) -> str:
    """Функция возвращает отфилтрованную дату"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


def mask_account_card(card_number: str) -> str:
    """Функция возращает номер счета и карты со скрытими символами"""
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