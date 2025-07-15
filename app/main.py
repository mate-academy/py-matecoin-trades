import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name, "r") as file:
        trades_info = json.load(file)

    for trade in trades_info:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = trade.get("matecoin_price")

        if bought is not None:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * Decimal(matecoin_price)

        if sold is not None:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(matecoin_price)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
