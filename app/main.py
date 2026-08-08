import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades_data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            cost = bought * matecoin_price
            earned_money -= cost
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            revenue = sold * matecoin_price
            earned_money += revenue
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
