import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = matecoin_account = 0

    with open(file_name, "r") as trades:
        trades = json.load(trades)

    for trade in trades:
        bought, sold, matecoin_price = trade.values()
        if bought:
            earned_money -= Decimal(bought) * Decimal(matecoin_price)
            matecoin_account += Decimal(bought)
        if sold:
            earned_money += Decimal(sold) * Decimal(matecoin_price)
            matecoin_account -= Decimal(sold)

    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}, f, indent=2)
