def get_date(date_str: str) -> str:
    """Функция возвращает отфилтрованную дату"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


def mask_account_card(card_number: str) -> str:
    """"""
    pass
