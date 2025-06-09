def filter_by_currency(transactions: list, currency: str):
    """Функция фильтрует транзакции по заданной валюте и возвращает итератор"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list):
    """Функция-Генератор, которая возвращает описания транзакций"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int):
    """Генератор номеров банковских карт в заданном диапазоне"""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted_card = " ".join([card_str[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card
