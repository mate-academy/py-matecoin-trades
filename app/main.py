import json
from decimal import Decimal
from tempfile import NamedTemporaryFile
from app.main import calculate_profit


def test_calculate_profit_runs_without_error() -> None:
    # Создаём временный trades.json
    trades_data = [
        {"bought": "0.00111", "sold": None, "matecoin_price": "48911.23"},
        {"bought": None, "sold": "0.00058", "matecoin_price": "77830.83"}
    ]

    # NamedTemporaryFile с delete=False, чтобы calculate_profit мог открыть файл
    with NamedTemporaryFile("w+", suffix=".json", delete=False) as temp_file:
        json.dump(trades_data, temp_file)
        temp_file_path = temp_file.name

    # Вызываем функцию с временным файлом
    calculate_profit(temp_file_path)

    # Проверяем, что создан файл profit.json
    with open("profit.json", "r", encoding="utf-8") as f:
        result = json.load(f)

    # Проверка, что ключи есть и значения корректного типа
    assert "earned_money" in result
    assert "matecoin_account" in result
    # Проверяем, что значения можно превратить в Decimal
    Decimal(result["earned_money"])
    Decimal(result["matecoin_account"])
