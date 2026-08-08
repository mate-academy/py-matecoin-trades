import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    count_coins = Decimal("0")
    profit = Decimal("0")

    with open(name_file, "r") as file:
        trades = json.load(file)

        for trade in trades:
            if trade["bought"] is not None:
                bought = Decimal(trade["bought"])
                price = Decimal(trade["matecoin_price"])

                count_coins += bought
                profit -= bought * price

            if trade["sold"] is not None:
                sold = Decimal(trade["sold"])
                price = Decimal(trade["matecoin_price"])

                count_coins -= sold
                profit += sold * price

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(count_coins)
            },
            file,
            indent=2
        )


if __name__ == "__main__":
    calculate_profit("trades.json")
