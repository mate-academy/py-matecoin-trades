import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades_data = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades_data:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if trade.get("bought") is not None:
            decimal_bought = Decimal(bought)

            matecoin_account += decimal_bought
            earned_money -= decimal_bought * matecoin_price

        if trade.get("sold") is not None:
            decimal_sold = Decimal(sold)

            matecoin_account -= decimal_sold
            earned_money += decimal_sold * matecoin_price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(project_root, "profit.json")
    with open(output_path, "w") as file:
        json.dump(profit, file, indent=2)
