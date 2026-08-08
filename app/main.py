import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file_path, "r") as file:
        trades = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount_bought = Decimal(trade["bought"])
            earned_money -= amount_bought * price
            matecoin_account += amount_bought

        if trade["sold"] is not None:
            amount_sold = Decimal(trade["sold"])
            earned_money += amount_sold * price
            matecoin_account -= amount_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
