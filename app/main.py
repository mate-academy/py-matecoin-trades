import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as f:
        data = json.load(f)
    if data is None:
        return
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in data:
        if trade["bought"]:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])
    total_profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as f:
        json.dump(total_profit_info, f, indent=4)
