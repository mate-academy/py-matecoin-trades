import json
from decimal import Decimal, getcontext
import os

getcontext().prec = 28


def calculate_profit(file_name: str) -> None:
    file_path = os.path.join(os.getcwd(), file_name)
    profit_file_path = os.path.join(os.getcwd(), "profit.json")

    try:
        with open(file_path, "r") as f:
            trades = json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_account += bought - sold
        if trade["bought"]:
            earned_money -= bought * Decimal(trade["matecoin_price"])
        if trade["sold"]:
            earned_money += sold * Decimal(trade["matecoin_price"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    try:
        with open(profit_file_path, "w") as f:
            json.dump(profit, f, indent=2)
        print(f"Profit calculated and saved to {profit_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


calculate_profit("trades.json")
