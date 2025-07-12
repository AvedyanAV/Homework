import json


def load_transactions(file_path):
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == '__main__':
    transactions = load_transactions('data/operations.json')
    print(transactions)


