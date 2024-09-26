import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Process each trade
    for trade in data:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            bought = Decimal(bought)
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if sold is not None:
            sold = Decimal(sold)
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
