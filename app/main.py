import json
from decimal import Decimal, getcontext
from typing import List, Dict


def calculate_profit(data: List[Dict[str, str]]) -> None:
    getcontext().prec = 10

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    total_spent = Decimal("0.0")

    with open(data, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            matecoin_account += Decimal(bought)
            total_spent += (Decimal(bought) * matecoin_price)

        if sold is not None:
            earned_money += (Decimal(sold) * matecoin_price)
            matecoin_account -= Decimal(sold)

    earned_money -= total_spent

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=2)


if __name__ == "__main__":
    with open("trades.json", "r") as f:
        data = json.load(f)
    calculate_profit(data)
