import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}", "r") as file_data:
        data = json.load(file_data)

        coins_bought = sum([Decimal(trade["bought"])
                            for trade in data if trade["bought"] is not None])
        coins_sold = sum([Decimal(trade["sold"])
                          for trade in data if trade["sold"] is not None])

        boughts_sum = sum(
            [Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
             for trade in data if trade["bought"] is not None]
        )
        solds_sum = sum(
            [Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
             for trade in data if trade["sold"] is not None]
        )

        result = {
            "earned_money": str(solds_sum - boughts_sum),
            "matecoin_account": str(coins_bought - coins_sold)
        }

    with open("profit.json", "w") as file_result:
        json.dump(result, file_result, indent=2)
