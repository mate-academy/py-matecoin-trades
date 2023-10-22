import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trade_data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trade_data:
        bought = trade.get("bought", None)
        sold = trade.get("sold", None)
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought = Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold is not None:
            sold = Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
