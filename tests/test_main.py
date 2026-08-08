import json
from decimal import Decimal
from tempfile import NamedTemporaryFile
from app.main import calculate_profit


def test_calculate_profit_runs_without_error() -> None:
    """Test that calculate_profit runs and creates profit.json correctly."""
    # Создаём тестовые данные
    trades_data = [
        {"bought": "0.00111", "sold": None, "matecoin_price": "48911.23"},
        {"bought": None, "sold": "0.00058", "matecoin_price": "77830.83"},
    ]

    # Создаём временный файл для trades.json
    with NamedTemporaryFile("w+", suffix=".json", delete=False) as temp_file:
        json.dump(trades_data, temp_file)
        temp_file_path = temp_file.name

    # Вызываем calculate_profit с временным файлом
    calculate_profit(temp_file_path)

    # Проверяем, что создан profit.json
    with open("profit.json", "r", encoding="utf-8") as f:
        result = json.load(f)

    # Проверяем ключи
    assert "earned_money" in result
    assert "matecoin_account" in result

    # Проверяем, что значения можно превратить в Decimal
    Decimal(result["earned_money"])
    Decimal(result["matecoin_account"])
