import json
from decimal import Decimal


def calculate_profit(trades_file: str ="") -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    count_in_dollars = 0
    count_matecoin = 0

    for trade in trades:
        if trade["bought"] is not None:
            count_in_dollars -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
            count_matecoin += Decimal(trade["bought"])
        if trade["sold"] is not None:
            count_in_dollars += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )
            count_matecoin -= Decimal(trade["sold"])


    result_dict = {
        "earned_money": str(count_in_dollars),
        "matecoin_account": str(count_matecoin),
    }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
