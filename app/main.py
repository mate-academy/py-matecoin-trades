import json
from decimal import Decimal


def calculate_profit(file_name: str) -> dict:
    with open(file_name) as f:
        trades = json.load(f)

    profit, mcoin = 0, 0
    for trade in trades:
        if trade["bought"]:
            profit -= Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])
            mcoin += Decimal(trade["bought"])
        if trade["sold"]:
            profit += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            mcoin -= Decimal(trade["sold"])

    profit_to_json = {"earned_money": str(profit),
                      "matecoin_account": str(mcoin)}

    with open("profit.json", "w") as f:
        json.dump(profit_to_json, f, indent=2)
