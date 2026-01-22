import json
from decimal import Decimal


def calculate_profit(json_path: str) -> None:
    with open(json_path, "r") as trade_file:
        trades = json.load(trade_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_volume = Decimal(bought)
            earned_money -= bought_volume * matecoin_price
            matecoin_account += bought_volume
        if sold is not None:
            sold_volume = Decimal(sold)
            earned_money += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
