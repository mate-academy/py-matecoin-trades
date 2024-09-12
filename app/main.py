import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(file_name) as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought", 0)
        sold = trade.get("sold", 0)
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought:
            earned_money -= Decimal(bought) * matecoin_price
            matecoin_account += Decimal(bought)

        if sold:
            earned_money += Decimal(sold) * matecoin_price
            matecoin_account -= Decimal(sold)

    trade_result = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as file:
        json.dump(trade_result, file, indent=2)
