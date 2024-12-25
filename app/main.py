import json
from decimal import Decimal

def calculate_profit(trades_file) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")
        matecoin_price = Decimal(trade["matecoin_price"])

        matecoin_account += bought - sold
        earned_money += (sold - bought) * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)

    return None
