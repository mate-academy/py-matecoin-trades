import json
from decimal import Decimal


def calculate_profit(trade_file: json) -> None:
    with open(trade_file, "r") as f:
        trades = json.load(f)
    result = 0
    total_bought = 0
    total_sold = 0
    for trade in trades:
        if trade["bought"]:
            total_bought += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            result += Decimal(trade["bought"])
        if trade["sold"]:
            total_sold += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
            result -= Decimal(trade["sold"])
    date_finish = {
        "earned_money": str(total_sold - total_bought),
        "matecoin_account": str(result)
    }
    with open("profit.json", "w") as file:
        json.dump(date_finish, file, indent=2)
