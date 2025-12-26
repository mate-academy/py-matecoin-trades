import json
from decimal import Decimal


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r") as file_name:
        trades = json.load(file_name)

    earned = Decimal("0")
    acc_balance = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = trade.get("bought")
        if bought is not None:
            vol = Decimal(bought)
            acc_balance += vol
            earned -= vol * price
        sold = trade.get("sold")
        if sold is not None:
            vol = Decimal(sold)
            acc_balance -= vol
            earned += vol * price

    result = {
        "earned_money": format(earned, "f"),
        "matecoin_account": format(acc_balance, "f"),
    }

    with open("profit.json", "w") as file_name:
        json.dump(result, file_name, indent=2)

calculate_profit("trades.json")