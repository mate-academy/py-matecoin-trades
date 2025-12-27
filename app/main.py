import json
from decimal import Decimal


def calculate_profit(trade_file: str) -> None:
    with open(trade_file, "r", encoding="utf-8") as trade:
        data = json.load(trade)
        earned_money, matecoin_account = 0, 0

        for info in data:
            if info["bought"] is not None:
                earned_money -= Decimal(info["bought"]) * \
                    Decimal(info["matecoin_price"])
                matecoin_account += Decimal(info["bought"])
            if info["sold"] is not None:
                earned_money += Decimal(info["sold"]) * \
                    Decimal(info["matecoin_price"])
                matecoin_account -= Decimal(info["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as output:
        json.dump(profit, output, indent=2)
