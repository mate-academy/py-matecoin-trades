import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as f:
        info_file = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in info_file:
        bought = Decimal(trade.get("bought", "0"))\
            if trade.get("bought") else Decimal("0")
        sold = Decimal(trade.get("sold", "0"))\
            if trade.get("sold") else Decimal("0")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        earned_money += (sold - bought) * matecoin_price
        matecoin_account += (bought - sold)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
