import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    print("sads")
    with open(trades_file, "r") as file:
        data = json.load(file)

    matecoin_account = 0
    earned_money = 0

    for trade in data:
        price = Decimal(trade["matecoin_price"])
        bought = (Decimal(trade["bought"]) * price
                  if trade["bought"] is not None else Decimal(0))
        sold = (Decimal(trade["sold"]) * price
                if trade["sold"] is not None else Decimal(0))

        matecoin_account += (bought - sold) / price
        earned_money += sold - bought

    info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as new_file:
        json.dump(info, new_file, indent=2)
