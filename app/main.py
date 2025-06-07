from decimal import Decimal
import json
import os

def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name, 'r') as f:
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
    profit_file = os.path.join(os.path.dirname(os.path.abspath(file_name)), "profit.json")
    with open(profit_file, "w") as f:
        json.dump(finish_result, f, indent=2)