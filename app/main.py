import json

from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file) as f:
        trades_datas = json.load(f)
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for data in trades_datas:
        matecoin_price = Decimal(data["matecoin_price"])

        if data["bought"] is not None:
            bought = Decimal(data["bought"])
            earned_money -= matecoin_price * bought
            matecoin_account += bought
        if data["sold"] is not None:
            sold = Decimal(data["sold"])
            earned_money += matecoin_price * sold
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
