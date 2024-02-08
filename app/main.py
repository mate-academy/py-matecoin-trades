import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    result = {
        "earned_money": str,
        "matecoin_account": str
    }
    sum_bought, sum_sold, sum_bought_dollars, sum_sold_dollars = 0, 0, 0, 0
    with open(trades_file) as file_in:
        trades_data = json.load(file_in)
    for trade in trades_data:
        if trade["bought"]:
            sum_bought += Decimal(trade["bought"])
            sum_bought_dollars += (Decimal(trade["bought"])
                                   * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            sum_sold += Decimal(trade["sold"])
            sum_sold_dollars += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))

    result["matecoin_account"] = str(sum_bought - sum_sold)
    result["earned_money"] = str(sum_sold_dollars - sum_bought_dollars)
    with open("profit.json", "w") as file_out:
        json.dump(result, file_out, indent=2)
