from decimal import Decimal
import json


def calculate_profit(name_file: str) -> None:
    with open(name_file) as file:
        user_date = json.load(file)

    bought = 0
    exchange_bought = 0
    sold = 0
    exchange_sold = 0

    for date in user_date:
        if date["bought"]:
            bought += Decimal(date["bought"])
            exchange_bought += (
                Decimal(date["bought"]) * Decimal(date["matecoin_price"])
            )

        if date["sold"]:
            sold += Decimal(date["sold"])
            exchange_sold += (
                Decimal(date["sold"]) * Decimal(date["matecoin_price"])
            )

    new_date = {
        "earned_money": str(exchange_sold - exchange_bought),
        "matecoin_account": str(bought - sold),
    }
    with open("profit.json", "w") as f:
        json.dump(new_date, f, indent=2)
