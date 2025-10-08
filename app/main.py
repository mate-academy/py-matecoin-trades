import json
from decimal import Decimal

def calculate_profit():
    with open("trades.json", "r") as f:
        trade = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for t in trade:
        if t["bought"] is not None:
            volume = Decimal(t["bought"])
            preco = Decimal(t["matecoin_price"])
            earned_money -= volume * preco
            matecoin_account += volume
        if t["sold"] is not None:
            volume = Decimal(t["sold"])
            preco = Decimal(t["matecoin_price"])
            earned_money += volume * preco
            matecoin_account -= volume

    trade_string = {"earned_money": str(earned_money), "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(trade_string, f)