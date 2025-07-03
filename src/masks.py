def get_mask_card_number(card_number: str | int) -> str:
    """Функция возвращает номер карты со скрытыми символами"""
    num_str = str(card_number)
    digits = ''
    for i in num_str:
        if i.isdigit():
            digits += i
    if len(str(digits)) != 16:
        return "Некорректный номер карты"

    return f"{str(digits)[:4]} {str(digits)[4:6]}** **** {str(digits)[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция возвращает номер счета со скрытыми символами"""
    num_str = str(account)
    digits = ''
    for i in num_str:
        if i.isdigit():
            digits += i
    if len(str(digits)) != 20:
        return "Некорректный номер счета"

    return str(f"**{str(digits)[-4:]}")
