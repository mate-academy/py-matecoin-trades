import decimal
import json


def calculate_profit(file_name: str) -> None:
    data = None
    with open(file_name, "r") as file:
        data = json.load(file)

    total_coins_bought = decimal.Decimal("0")
    total_spent = decimal.Decimal("0")
    total_coins_sold = decimal.Decimal("0")
    total_earned = decimal.Decimal("0")

    for transaction in data:
        if transaction["bought"]:
            bought = decimal.Decimal(transaction["bought"])
            total_coins_bought += bought
            price = decimal.Decimal(transaction["matecoin_price"])
            total_spent += bought * price

        if transaction["sold"]:
            sold = decimal.Decimal(transaction["sold"])
            total_coins_sold += sold
            price = decimal.Decimal(transaction["matecoin_price"])
            total_earned += sold * price

    profit = total_earned - total_spent
    coins = total_coins_bought - total_coins_sold

    profit_data = {
        "earned_money": str(profit),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
