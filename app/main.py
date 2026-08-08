from decimal import Decimal
import json


def calculate_profit(name: str = "trades.json") -> None:
    with open(name) as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        price_metacoin = Decimal(trade["matecoin_price"])
        bought = trade.get("bought", 0)
        sold = trade.get("sold", 0)
        if bought:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * price_metacoin
        if sold:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * price_metacoin

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
