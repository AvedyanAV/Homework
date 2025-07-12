from src.external_api import get_transaction_amount_in_rub
import pytest
from unittest.mock import patch, MagicMock
import requests


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


def test_rub_transaction_no_conversion(rub_transaction):
    """Тест транзакции в рублях без конвертации"""
    with patch('requests.get') as mock_get:
        result = get_transaction_amount_in_rub(rub_transaction)
        assert result == 1000.0
        mock_get.assert_not_called()


def test_usd_transaction_conversion(usd_transaction):
    """Тест конвертации USD в RUB"""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "rates": {
            "USD": 0.011,
            "EUR": 0.009
        }
    }

    with patch('requests.get', return_value=mock_response) as mock_get:
        result = get_transaction_amount_in_rub(usd_transaction)
        assert round(result, 2) == 9090.91
        mock_get.assert_called_once_with(
            'https://api.exchangerate-api.com/v4/latest/RUB',
            timeout=10
        )


def test_api_request_failure(usd_transaction):
    """Тест ошибки запроса к API"""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API недоступен")

        with pytest.raises(ValueError) as excinfo:
            get_transaction_amount_in_rub(usd_transaction)

        assert "Ошибка при получении курса валют: API недоступен" in str(excinfo.value)

        mock_get.assert_called_once_with(
            'https://api.exchangerate-api.com/v4/latest/RUB',
            timeout=10
        )


def test_invalid_api_response(usd_transaction):
    """Тест невалидного ответа API"""
    mock_response = MagicMock()
    mock_response.json.return_value = {"invalid": "response"}

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError) as excinfo:
            get_transaction_amount_in_rub(usd_transaction)
        assert "Не удалось получить курс для указанной валюты" in str(excinfo.value)
