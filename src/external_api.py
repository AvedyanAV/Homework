import requests


def get_transaction_amount_in_rub(transaction):
    """
    Возвращает сумму транзакции в рублях.
    Если валюта не RUB, конвертирует по текущему курсу через API.
    """
    try:
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

        response = requests.get(
            'https://api.exchangerate-api.com/v4/latest/RUB',
            timeout=10
        )
        response.raise_for_status()
        rates = response.json()['rates']

        rate = 1 / rates[currency]
        return round(float(amount) * rate, 2)

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка при получении курса валют: {str(e)}")

    except KeyError:
        raise ValueError("Не удалось получить курс для указанной валюты")
