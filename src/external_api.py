import requests
from dotenv import load_dotenv
import os


load_dotenv()

headers = {"apikey": os.getenv('API_KEY')}


def get_transaction_amount_in_rub(transaction):
    """
    Возвращает сумму транзакции в рублях.
    Если валюта не RUB, конвертирует по текущему курсу через API.
    """
    try:
        # Проверка наличия API ключа
        if not headers.get('apikey'):
            raise ValueError("API ключ не настроен. Проверьте .env файл")

        operation_amount = transaction.get('operationAmount')
        if not operation_amount:
            raise ValueError("Транзакция должна содержать operationAmount")

        amount = operation_amount.get('amount')
        currency_info = operation_amount.get('currency')

        if amount is None or currency_info is None:
            raise ValueError("Транзакция должна содержать amount и currency")

        currency = currency_info.get('code')
        if currency is None:
            raise ValueError("Валюта должна содержать code")

        if currency == 'RUB':
            return float(amount)

        if currency not in ('USD', 'EUR'):
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        result = response.json()
        if not result.get('success', False):
            raise ValueError("Ошибка конвертации валюты")

        return float(result['result'])

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка при получении курса валют: {str(e)}")
    except KeyError:
        raise ValueError("Не удалось получить курс для указанной валюты")
