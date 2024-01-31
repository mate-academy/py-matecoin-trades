import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = 0
    matecoin_account = 0

    with open(file_name) as file:
        trades = json.load(file)

        for trade in trades:
            if trade["bought"] is None:
                trade["bought"] = 0
            elif trade["sold"] is None:
                trade["sold"] = 0

            profit = (
                profit
                - (Decimal(trade["bought"]) * Decimal(trade["matecoin_price"]))
                + (Decimal(trade["sold"]) * Decimal(trade["matecoin_price"]))
            )

            matecoin_account = matecoin_account + (
                Decimal(trade["bought"]) - Decimal(trade["sold"])
            )

    profit_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as result_file:
        json.dump(profit_dict, result_file, indent=2)
