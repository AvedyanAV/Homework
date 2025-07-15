import pytest
from unittest.mock import patch, MagicMock
import requests
from src.external_api import get_transaction_amount_in_rub
import os


headers = {"apikey": os.getenv('API_KEY')}


@pytest.fixture
def rub_transaction():
    return {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "code": "RUB",
                "name": "рубль"
            }
        }
    }


@pytest.fixture
def usd_transaction():
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD",
                "name": "доллар США"
            }
        }
    }


@pytest.fixture
def eur_transaction():
    return {
        "operationAmount": {
            "amount": "50.00",
            "currency": {
                "code": "EUR",
                "name": "евро"
            }
        }
    }


@pytest.fixture
def invalid_transaction_missing_amount():
    return {
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    }


@pytest.fixture
def invalid_transaction_unsupported_currency():
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "GBP",
                "name": "фунт стерлингов"
            }
        }
    }


@pytest.fixture
def mock_api_key(monkeypatch):
    monkeypatch.setitem(headers, 'apikey', 'test_api_key')


def test_rub_transaction_no_conversion(rub_transaction, mock_api_key):
    """Тест транзакции в рублях без конвертации"""
    with patch('requests.get') as mock_get:
        result = get_transaction_amount_in_rub(rub_transaction)
        assert result == 1000.0
        mock_get.assert_not_called()


def test_missing_operation_amount(mock_api_key):
    """Тест отсутствия operationAmount"""
    with pytest.raises(ValueError) as excinfo:
        get_transaction_amount_in_rub({"invalid": "data"})
    assert "Транзакция должна содержать operationAmount" in str(excinfo.value)


def test_missing_amount_field(invalid_transaction_missing_amount, mock_api_key):
    """Тест отсутствия amount"""
    with pytest.raises(ValueError) as excinfo:
        get_transaction_amount_in_rub(invalid_transaction_missing_amount)
    assert "Транзакция должна содержать amount и currency" in str(excinfo.value)


def test_missing_currency_code(mock_api_key):
    """Тест отсутствия кода валюты"""
    invalid_transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"name": "рубль"}
        }
    }
    with pytest.raises(ValueError) as excinfo:
        get_transaction_amount_in_rub(invalid_transaction)
    assert "Валюта должна содержать code" in str(excinfo.value)


def test_unsupported_currency(invalid_transaction_unsupported_currency, mock_api_key):
    """Тест неподдерживаемой валюты"""
    with patch('requests.get') as mock_get:
        with pytest.raises(ValueError) as excinfo:
            get_transaction_amount_in_rub(invalid_transaction_unsupported_currency)
        assert "Неподдерживаемая валюта: GBP" in str(excinfo.value)
        mock_get.assert_not_called()


def test_api_request_failure(usd_transaction, mock_api_key):
    """Тест ошибки запроса к API"""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API недоступен")

        with pytest.raises(ValueError) as excinfo:
            get_transaction_amount_in_rub(usd_transaction)
        assert "Ошибка при получении курса валют: API недоступен" in str(excinfo.value)


def test_invalid_api_response(usd_transaction, mock_api_key):
    """Тест невалидного ответа API"""
    mock_response = MagicMock()
    mock_response.json.return_value = {"success": False}

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError) as excinfo:
            get_transaction_amount_in_rub(usd_transaction)
        assert "Ошибка конвертации валюты" in str(excinfo.value)
