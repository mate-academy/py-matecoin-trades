import json
from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            bought_volume = Decimal(bought)
            earned_money -= bought_volume * matecoin_price
            matecoin_account += bought_volume

        if sold is not None:
            sold_volume = Decimal(sold)
            earned_money += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
