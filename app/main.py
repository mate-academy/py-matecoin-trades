import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    if trades is not None and len(trades) != 0:
        for trade in trades:
            if "bought" in trade.keys() and trade["bought"] is not None:
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])
            if "sold" in trade.keys() and trade["sold"] is not None:
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

    summary = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(summary, file, indent=2)
