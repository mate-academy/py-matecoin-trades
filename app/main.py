import json
from decimal import Decimal


def calculate_profit(file_name: json) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    bought = 0
    sold = 0
    metacoin_account = 0
    for trade in trades:
        if trade["bought"]:
            bought += Decimal(trade["bought"])
            metacoin_account -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            sold += Decimal(trade["sold"])
            metacoin_account += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
    profit = {
        "earned_money": str(metacoin_account),
        "matecoin_account": str(bought - sold),
    }
    with open("../profit.json", "w") as file:
        json.dump(profit, file, indent=2)
    return None
