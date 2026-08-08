import json


from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"] or 0)
        sold = Decimal(trade["sold"] or 0)
        matecoin_account += bought - sold
        earned_money += (sold - bought) * Decimal(trade["matecoin_price"])

    matecoin_account = str(matecoin_account)
    earned_money = str(earned_money)
    result = {"earned_money": earned_money,
              "matecoin_account": matecoin_account}

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
