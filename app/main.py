import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        bought = trade.get("bought")
        sold = trade.get("sold")

        if bought is not None:
            bought = Decimal(bought)
            matecoin_account = matecoin_account + bought
            earned_money = earned_money - (bought * price)

        if sold is not None:
            sold = Decimal(sold)
            matecoin_account = matecoin_account - sold
            earned_money = earned_money + (sold * price)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as g:
        json.dump(result, g, indent=2)
