import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    try:
        with open(file_name, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File: {file_name} not found")
        return
    except json.JSONDecodeError:
        print(f"File: {file_name} is not a valid JSON file")
        return

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:

        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    finish_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(finish_result, f, indent=2)
