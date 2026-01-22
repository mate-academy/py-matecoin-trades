import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        bought = decimal.Decimal(trade["bought"] or "0")
        sold = decimal.Decimal(trade["sold"] or "0")
        price = decimal.Decimal(trade["matecoin_price"])

        earned_money += (sold - bought) * price
        matecoin_account += bought - sold

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
