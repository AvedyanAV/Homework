import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_usd_transactions(transactions: list) -> None:
    """Тест фильтрации USD-транзакций"""
    usd_transactions = filter_by_currency(transactions, "USD")
    assert list(usd_transactions)


def test_filter_rub_transactions(transactions: list) -> None:
    """Тест фильтрации RUB-транзакций"""
    rub_transactions = filter_by_currency(transactions, "RUB")
    assert list(rub_transactions)


def test_filter_transactions_zero(transactions: list) -> None:
    """Тест фильтрации пустого списка"""
    transactions_zero = filter_by_currency([], "USD")
    assert transactions_zero


def test_transaction_descriptions(transactions: list) -> None:
    """Тест генератора который возвращает описания транзакций"""
    transaction = transaction_descriptions(transactions)
    return transaction


def test_small_range() -> None:
    """Тест с маленькими числами"""
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"


def test_large_numbers() -> None:
    """Тест с большими числами"""
    gen = card_number_generator(9999999999999996, 9999999999999999)
    assert next(gen) == "9999 9999 9999 9996"
    assert next(gen) == "9999 9999 9999 9997"
    assert next(gen) == "9999 9999 9999 9998"
    assert next(gen) == "9999 9999 9999 9999"


def test_format_correctness() -> None:
    """Тест корректности форматирования"""
    gen = card_number_generator(1234567812345678, 1234567812345678)
    assert next(gen) == "1234 5678 1234 5678"
