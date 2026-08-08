import json
from decimal import Decimal
from pathlib import Path

PROFIT_PATH = Path(__file__).resolve().parent.parent / "profit.json"


def calculate_profit(trades_file_path: str) -> None:
    total_spent = Decimal("0")
    total_received = Decimal("0")
    balance = Decimal("0")

    with open(trades_file_path, "r") as file_trade:
        trades = json.load(file_trade)
        for i in trades:
            price = Decimal(i["matecoin_price"])
            if i.get("bought") is not None:
                amount = Decimal(i["bought"])
                total_spent += amount * price
                balance += amount
            if i.get("sold") is not None:
                amount = Decimal(i["sold"])
                total_received += amount * price
                balance -= amount

    earned_money = total_received - total_spent

    # Створюємо словник зі значеннями у вигляді рядків (як вимагає тест)
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(balance)
    }

    # Записуємо за правильним шляхом
    with open(PROFIT_PATH, "w") as file_profit:
        json.dump(profit, file_profit, indent=2)
