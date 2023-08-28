import json
import decimal


def calculate_profit(name: str) -> None:
    with open(name) as file:
        trades = json.load(file)
    earn_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)
    for trade in trades:
        if trade.get("bought"):
            earn_money -= (decimal.Decimal(trade.get("bought"))
                           * decimal.Decimal(trade.get("matecoin_price")))
            matecoin_account += decimal.Decimal(trade.get("bought"))
        if trade.get("sold"):
            earn_money += (decimal.Decimal(trade.get("sold"))
                           * decimal.Decimal(trade.get("matecoin_price")))
            matecoin_account -= decimal.Decimal(trade.get("sold"))

    profit = {
        "earned_money": str(earn_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
