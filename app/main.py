import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            matecoin += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])

        if trade["sold"] is not None:
            matecoin -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin)
              }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
