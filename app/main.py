import json
from decimal import Decimal


def calculate_profit(data_file: str) -> None:
    profit = Decimal("0.0")
    amount = Decimal("0.0")
    with (open(data_file) as f):
        trades = json.load(f)
        for trade in trades:
            if trade["bought"]:
                profit -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
                amount += Decimal(trade["bought"])
            if trade["sold"]:
                profit += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
                amount -= Decimal(trade["sold"])

    result_data = {
        "earned_money": str(profit),
        "matecoin_account": str(amount)
    }
    with open("profit.json", "w") as f_prof:
        json.dump(result_data, f_prof, indent=2)
