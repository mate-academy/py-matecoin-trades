import os
import json
import decimal


def calculate_profit(file_name: str) -> None:
    if not os.path.exists(file_name) or not file_name.endswith(".json"):
        print("Invalid file. Please provide a valid JSON file.")
        return

    with open(file_name, "r") as file:
        data = json.load(file)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in data:
        matecoin_price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"]:
            earned_money -= decimal.Decimal(trade["bought"]) * matecoin_price
            matecoin_account += decimal.Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += decimal.Decimal(trade["sold"]) * matecoin_price
            matecoin_account -= decimal.Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
