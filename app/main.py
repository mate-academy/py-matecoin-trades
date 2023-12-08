import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:

    with open("/Users/rurakite/PycharmProjects/"
              "py-matecoin-trades/app/trades.json", "r") as f:
        trades = json.load(f)
    sold = Decimal("0.0")
    bought = Decimal("0.0")
    sold_coins_amount = 0
    bought_coins_amount = 0

    for trade in trades:
        if trade["sold"]:
            sold += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            sold_coins_amount += Decimal(trade["sold"])

        if trade["bought"]:
            bought += (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            bought_coins_amount += Decimal(trade["bought"])

    earned_money = sold - bought
    matecoin_account = bought_coins_amount - sold_coins_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("/Users/rurakite/PycharmProjects/"
              "py-matecoin-trades/profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)

# calculate_profit()
