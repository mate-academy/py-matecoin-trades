import json
from decimal import Decimal


def calculate_profit(profit: str) -> None:
    with open(profit, "r") as file:
        trades = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal("0")
        price = Decimal(trade["matecoin_price"])
        matecoin_account += bought - sold
        earned_money += (sold * price) - (bought * price)
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
