import json
from decimal import Decimal


def calculate_profit(path_to_file: str) -> None:
    costs = Decimal("0")
    received = Decimal("0")
    sum_bought = Decimal("0")
    sum_sold = Decimal("0")

    with open(path_to_file) as json_data:
        matecoin_data = json.load(json_data)
        for matecoin in matecoin_data:
            if matecoin["bought"]:
                bought = Decimal(matecoin["bought"])
                price_bought = Decimal(matecoin["matecoin_price"])
                costs += bought * price_bought
                sum_bought += bought

            if matecoin["sold"]:
                sold = Decimal(matecoin["sold"])
                price_sold = Decimal(matecoin["matecoin_price"])
                received += sold * price_sold
                sum_sold += sold

        profit = {
            "earned_money": str(received - costs),
            "matecoin_account": str(sum_bought - sum_sold)
        }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
