import decimal
import json
import os


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    total_coins_bought = decimal.Decimal("0")
    total_spent = decimal.Decimal("0")
    total_coins_sold = decimal.Decimal("0")
    total_earned = decimal.Decimal("0")

    for transaction in transactions:
        if transaction["bought"]:
            bought = decimal.Decimal(transaction["bought"])
            price = decimal.Decimal(transaction["matecoin_price"])
            total_coins_bought += bought
            total_spent += bought * price
        if transaction["sold"]:
            sold = decimal.Decimal(transaction["sold"])
            price = decimal.Decimal(transaction["matecoin_price"])
            total_coins_sold += sold
            total_earned += sold * price

    profit = total_earned - total_spent
    current_coins = total_coins_bought - total_coins_sold

    data = {"earned_money": str(profit),
            "matecoin_account": str(current_coins)
            }

    parent_dir_path = os.path.join("", "profit.json")
    with open(parent_dir_path, "w") as file:
        json.dump(data, file, indent=2)
