import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        trades = json.load(json_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        for item in ("bought", "sold", "matecoin_price"):
            trade[item] = Decimal(
                trade.get(item, "0") if trade.get(item, "0") else "0"
            )
        earned_money += ((trade["sold"] - trade["bought"])
                         * trade["matecoin_price"])
        matecoin_account += trade["bought"] - trade["sold"]

    with open("profit.json", "w") as json_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            json_file,
            indent=2
        )
