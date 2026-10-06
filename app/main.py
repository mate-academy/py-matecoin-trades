from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, encoding="utf-8") as source:
        trades = json.load(source)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")
        price = Decimal(trade["matecoin_price"])
        matecoin_account += bought - sold
        earned_money += (sold - bought) * price
    with open("profit.json", "w", encoding="utf-8") as output:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            output,
            indent=2,
        )
