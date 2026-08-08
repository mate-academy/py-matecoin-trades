import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name) as file:
            trades_data = json.load(file)
            print(trades_data)
    except FileNotFoundError:
        print(f"File: {file} not found")
    except json.JSONDecodeError:
        print(f"File {file} is not valid json")

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for data in trades_data:
        price = Decimal(data["matecoin_price"])
        if data["bought"] is not None:
            amount = Decimal(data["bought"])
            earned_money -= amount * price
            matecoin_account += amount
        if data["sold"] is not None:
            amount = Decimal(data["sold"])
            earned_money += amount * price
            matecoin_account -= amount
    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as js_file:
        json.dump(result, js_file, allow_nan=False, indent=2)
