import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_json_trades:
        response = json.load(file_json_trades)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    total_coin_balance = Decimal("0")

    for case in response:
        boughts = Decimal(case["bought"] or "0")
        solds = Decimal(case["sold"] or "0")
        price = Decimal(case["matecoin_price"])

        total_bought += boughts * price
        total_sold += solds * price
        total_coin_balance += boughts - solds

    result = {
        "earned_money": str(total_sold - total_bought),
        "matecoin_account": str(total_coin_balance)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
