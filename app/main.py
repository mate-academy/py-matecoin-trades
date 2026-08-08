import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as file:
        trades = json.load(file)
    profit = Decimal("0.0")
    matecoins = Decimal("0.0")
    for trade in trades:
        if trade.get("bought") is not None:
            profit -= (Decimal(trade["matecoin_price"])
                       * Decimal(trade["bought"]))
            matecoins += Decimal(trade["bought"])
        if trade.get("sold") is not None:
            profit += (Decimal(trade["matecoin_price"])
                       * Decimal(trade["sold"]))
            matecoins -= Decimal(trade["sold"])
    with open("profit.json", "w") as file:
        json.dump({"earned_money": str(Decimal(profit)),
                   "matecoin_account": str(Decimal(matecoins))},
                  file, indent=2)
