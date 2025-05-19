def get_mask_card_number(card_number: int) -> str:
    """Функция возращает номер карты со скрытими символами"""
    if len(str(card_number)) != 16:
        return "Некорректный номер карты"

    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция возращает номер счета со скрытими символами"""
    if len(str(account)) != 20:
        return "Некорректный номер счета"

    return str(f"**{str(account)[-4:]}")
