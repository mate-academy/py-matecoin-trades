import json
from decimal import Decimal


def calculate_profit(trades: dict):
    with open("trades.json", "r") as file:
        trade = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trade:
        if trade["bought"] is not None:
            volume = Decimal(trade["bought"])
            preco = Decimal(trade["matecoin_price"])
            earned_money -= volume * preco
            matecoin_account += volume
        if trade["sold"] is not None:
            volume = Decimal(trade["sold"])
            preco = Decimal(trade["matecoin_price"])
            earned_money += volume * preco
            matecoin_account -= volume

    trade_string = {"earned_money": str(earned_money), "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(trade_string, file)
