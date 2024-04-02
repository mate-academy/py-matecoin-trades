import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    matecoin_account = 0
    earned_money = 0
    result: dict

    with open(file_name, "r") as trades_json:
        trades = json.load(trades_json)

    for trade in trades:
        price = Decimal(trade.get("matecoin_price"))
        bought = Decimal(trade["bought"]) if trade["bought"] else 0
        sold = Decimal(trade["sold"]) if trade["sold"] else 0

        matecoin_account += bought - sold
        earned_money += (sold - bought) * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_json:
        json.dump(result, profit_json, indent=2)
