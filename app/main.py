import json
from decimal import Decimal
import os


def calculate_profit(filename: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

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
    result = {
        "earned_money": f"{earned_money:f}",
        "matecoin_account": f"{matecoin_account:f}"
    }

    # Write to profit.json
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


def main() -> None:
    # Get the folder containing this script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Join it with the filename
    file_path = os.path.join(base_dir, "trades.json")
    calculate_profit(file_path)


if __name__ == "__main__":
    main()
