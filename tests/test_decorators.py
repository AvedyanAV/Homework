import pytest
from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5

    captured = capsys.readouterr()

    assert "add started with args:(2, 3), kwargs:{}" in captured.out
    assert "add finished with result: 5" in captured.out


def test_log_to_console_error(capsys):
    """Тест ошибки с выводом в консоль"""

    @log()
    def add(a, b):
        return a + b

    with pytest.raises(TypeError):
        add(2, '3')

    captured = capsys.readouterr()

    assert "started with args:(2, '3'), kwargs:{}" in captured.out
    assert "failed with error:TypeError" in captured.out


def test_log_to_file_success(tmp_path):
    """Тест успешного выполнения с записью в файл"""
    log_dir = tmp_path / "tests"
    log_dir.mkdir()
    log_file = log_dir / "mylog.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "started with args:(2, 3), kwargs:{}" in content
        assert "finished with result: 5" in content


def test_log_to_file_error(tmp_path):
    """Тест ошибки с записью в файл"""
    log_dir = tmp_path / "tests"
    log_dir.mkdir()
    log_file = log_dir / "mylog.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    with pytest.raises(TypeError):
        add(2, '3')

    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "started with args:(2, '3'), kwargs:{}" in content
        assert "failed with error:TypeError" in content
