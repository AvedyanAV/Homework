import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8', mode='w')
file_formator = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formator)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str | int) -> str:
    """Функция возвращает номер карты со скрытыми символами"""
    logger.info('Функция начала обработку номера карты')
    num_str = str(card_number)
    digits = ''
    for i in num_str:
        if i.isdigit():
            digits += i
    if len(str(digits)) != 16:
        logger.error('Произошла ошибка: Некорректный номер карты')
        return "Некорректный номер карты"

    logger.info('Функция успешно выполнила скрытие символов карты')
    return f"{str(digits)[:4]} {str(digits)[4:6]}** **** {str(digits)[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция возвращает номер счета со скрытыми символами"""
    logger.info('Функция начала обработку номера счета')
    num_str = str(account)
    digits = ''
    for i in num_str:
        if i.isdigit():
            digits += i
    if len(str(digits)) != 20:
        logger.error('Произошла ошибка: Некорректный номер счета')
        return "Некорректный номер счета"

    logger.info('Функция успешно выполнила скрытие символов счета')
    return str(f"**{str(digits)[-4:]}")
