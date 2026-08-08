import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as f:
        trades = json.load(f)
    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = trade["matecoin_price"]

        if bought is not None:
            earned_money -= Decimal(bought) * Decimal(matecoin_price)
            matecoin_account += Decimal(bought)
        if sold is not None:
            earned_money += Decimal(sold) * Decimal(matecoin_price)
            matecoin_account -= Decimal(sold)

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as f_profit:
        json.dump(profit_dict, f_profit, indent=2)
