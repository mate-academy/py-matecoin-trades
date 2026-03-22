import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    with open(filename) as file:
        trades = json.load(file)

    earned_money = []
    coin_account = []
    for trade in trades:
        bought = (
            Decimal("0") if trade["bought"] is None
            else Decimal(trade["bought"])
        )
        sold = (
            Decimal("0") if trade["sold"] is None
            else Decimal(trade["sold"])
        )
        coin_price = Decimal(trade["matecoin_price"])
        earned_money.append(
            (sold * coin_price) - (bought * coin_price)
        )
        coin_account.append(bought - sold)

    profit = {
        "earned_money": str(sum(earned_money)),
        "matecoin_account": str(sum(coin_account))
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
