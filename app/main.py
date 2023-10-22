import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)
    money = 0
    matecoins = 0
    for trade in trades:
        if "bought" in trade and trade["bought"] is not None:
            money -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"])
            matecoins += Decimal(trade["bought"])
        if "sold" in trade and trade["sold"] is not None:
            money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoins -= Decimal(trade["sold"])
    profit_dict = {
        "earned_money": str(money),
        "matecoin_account": str(matecoins)
    }
    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
