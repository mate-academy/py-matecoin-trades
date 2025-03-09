import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name) as f:
        trade_data = json.load(f)

    for trade in trade_data:
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("../profit.json", "w", ) as f:
        json.dump(profit, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
