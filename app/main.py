import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades, "r") as f:
        data = json.load(f)
    for trade in data:
        if trade["bought"] is None:
            earned_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])
        else :
            earned_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])
    result = {
        "earned_money":str(earned_money),
        "matecoin_account":str(matecoin_account),
            }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)