import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(name) as t:
        trades = json.load(t)

    for trade in trades:
        matecoin_price = Decimal(trade.get("matecoin_price"))
        bought = trade.get("bought", 0)
        sold = trade.get("sold", 0)
        if bought:
            earned_money -= Decimal(bought) * matecoin_price
            matecoin_account += Decimal(bought)
        if sold:
            earned_money += Decimal(sold) * matecoin_price
            matecoin_account -= Decimal(sold)

    profit = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as new_file:
        json.dump(profit, new_file, indent=2)
