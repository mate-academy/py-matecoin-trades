# write your code here
import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    """
    Считает прибыль и остаток Matecoin по данным из trades_file
    и сохраняет результат в profit.json
    """
    # 1. Читаем данные из JSON-файла
    with open(trades_file, "r") as f:
        trades = json.load(f)  # превращаем JSON в Python список словарей

    # 2. Инициализируем баланс и прибыль
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    # 3. Проходим по каждой сделке
    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            amount = Decimal(bought)
            matecoin_account += amount
            earned_money -= amount * price  # потраченные деньги на покупку

        if sold is not None:
            amount = Decimal(sold)
            matecoin_account -= amount
            earned_money += amount * price  # заработанные деньги на продаже

    # 4. Формируем результат (все числа в виде строк!)
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # 5. Сохраняем результат в profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)

# Пример использования:
# calculate_profit("trades.json")
