import json
from decimal import Decimal
from typing import Any, Dict, List


def calculate_profit(file_name: str) -> Dict[str, str]:
    """Calculates Matecoin profit and writes result to profit.json."""

    # Загружаем данные из входного JSON
    with open(file_name, "r", encoding="utf-8") as file:
        trades: List[Dict[str, Any]] = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Обрабатываем каждую сделку
    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        # Если была покупка
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price

        # Если была продажа
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    # Формируем результат — значения должны быть строками!
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Сохраняем в profit.json
    with open("profit.json", "w", encoding="utf-8") as output:
        json.dump(result, output, indent=2)

    return result
