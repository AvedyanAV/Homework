import pytest
import json
from src.utils import load_transactions
from unittest.mock import mock_open, patch


@pytest.fixture
def valid_data():
    return [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@pytest.fixture
def non_list_data():
    return {"transactions": []}


def test_load_valid_transactions(valid_data):
    """Тест загрузки валидных данных"""
    m = mock_open(read_data=json.dumps(valid_data))
    with patch("builtins.open", m):
        result = load_transactions("test.json")
        assert result == valid_data
        m.assert_called_once_with("test.json", "r", encoding="utf-8")


def test_load_non_list_data(non_list_data):
    """Тест загрузки не-списка"""
    m = mock_open(read_data=json.dumps(non_list_data))
    with patch("builtins.open", m):
        result = load_transactions("test.json")
        assert result == []
        m.assert_called_once_with("test.json", "r", encoding="utf-8")


def test_file_not_found():
    """Тест отсутствия файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("nonexistent.json")
        assert result == []
