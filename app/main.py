import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename) as f:
        trade_deal = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trade_deal:
        if trade["bought"]:
            earned_money -= Decimal(
                trade["bought"]) * \
                Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += Decimal(
                trade["sold"]) * \
                Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as result_file:
        json.dump(profit, result_file, indent=2)
