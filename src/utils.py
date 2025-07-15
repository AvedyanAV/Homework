import json
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8', mode='w')
file_formator = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formator)
logger.addHandler(file_handler)


def load_transactions(file_path) -> list:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        logger.info(f'Произошла загрузка финансовых транзакций из JSON-файла:{file_path}')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f'Функция успешно загрузила данные из JSON-файла:{file_path}')
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f'Произошла ошибка: {FileNotFoundError}')
        return []
