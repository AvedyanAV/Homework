from datetime import datetime


def log(filename=None):
    """Декоратор логирует начало выполнения функции, её завершение или ошибку.
    Может выводить логи в консоль или записывать в файл"""
    def decorator(func):
        def wrapper(*args,  **kwargs):
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message_start = f"{start_time} - {func.__name__} started with args:{args}, kwargs:{kwargs}\n"

            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(log_message_start)
            else:
                print(log_message_start, end='')

            try:
                result = func(*args, **kwargs)

                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message_success = f"{end_time} - {func.__name__} finished with result: {result}\n"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message_success)
                else:
                    print(log_message_success, end='')

                return result

            except Exception as e:
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message_error = (f"{end_time} - {func.__name__} "
                                     f"failed with error:{type(e).__name__}, args:{args}, kwargs:{kwargs}\n")

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message_error)
                else:
                    print(log_message_error, end='')

                raise

        return wrapper

    return decorator


