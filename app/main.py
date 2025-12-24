import json
from decimal import Decimal


def calculate_profit(file_name):
    bought = Decimal("0")
    sold = Decimal("0")
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_name) as f:
        file_date = json.load(f)

    for d in file_date:
        if d["bought"]:
            bought += Decimal(d["bought"]) * Decimal(d["matecoin_price"])
            profit["matecoin_account"] += Decimal(d["bought"])
        if d["sold"]:
            sold += Decimal(d["sold"]) * Decimal(d["matecoin_price"])
            profit["matecoin_account"] -= Decimal(d["sold"])
    profit["earned_money"] = str(bought - sold)
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as profit_report:
        json.dump(profit, profit_report, indent=2)
