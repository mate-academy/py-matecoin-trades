import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought is not None:
            earned_money -= Decimal(bought) * matecoin_price
            matecoin_account += Decimal(bought)
        if sold is not None:
            earned_money += Decimal(sold) * matecoin_price
            matecoin_account -= Decimal(sold)

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
