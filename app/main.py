import json
from decimal import Decimal
import os


def calculate_profit(filename: str) -> dict:
    matecoin_account = 0
    earned_money = 0

    with open(filename) as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"] is not None:
            # Process bought trade
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])

        if trade["sold"] is not None:
            # Process sold trade
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * \
                Decimal(trade["matecoin_price"])
    return {
        "earned_money": f"{earned_money:f}",
        "matecoin_account": f"{matecoin_account:f}"
    }


def main() -> None:
    # Get the folder containing this script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Join it with the filename
    file_path = os.path.join(base_dir, "trades.json")
    profit = calculate_profit(file_path)

    with open(os.path.join(base_dir, "profit.json"), "w") as output_file:
        json.dump(profit, output_file)


if __name__ == "__main__":
    main()
