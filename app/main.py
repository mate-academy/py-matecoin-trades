import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    profit = 0
    matecoin_count = 0
    for trade in trades:
        if trade["bought"]:
            profit -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
            matecoin_count += Decimal(trade["bought"])
        if trade["sold"]:
            profit += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_count -= Decimal(trade["sold"])

    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(profit),
                   "matecoin_account": str(matecoin_count)},
                  fp=f,
                  indent=2)
