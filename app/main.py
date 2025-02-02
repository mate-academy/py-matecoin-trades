import json
import os
# import ast
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    try:
        with open(file_name, "r") as file:
            trades = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: File not found, unable to open or invalid json format")
        return

    profit = 0
    crypto = 0

    for trade in trades:
        if (trade["bought"]):
            profit -= Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])
            crypto += Decimal(trade["bought"])
        if (trade["sold"]):
            profit += Decimal(trade["sold"]) * \
                Decimal(trade["matecoin_price"])
            crypto -= Decimal(trade["sold"])

    data = {"earned_money": str(profit), "matecoin_account": str(crypto)}
    file_out = os.path.join(os.path.dirname(__file__), "..", "profit.json")

    try:
        with open(file_out, "w") as file_profit:
            json.dump(data, file_profit, indent=2)
    except IOError:
        print(f"Error: Write to file {file_out} failed")


if __name__ == "__main__":
    calculate_profit("app/trades.json")
