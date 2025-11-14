import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        traders = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in traders:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            volume = Decimal(trade["bought"])
            earned_money -= volume * price
            matecoin_account += volume
        if trade["sold"] is not None:
            volume_sold = Decimal(trade["sold"])
            earned_money += volume_sold * price
            matecoin_account -= volume_sold
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("../profit.json", "w") as f:
        json.dump(result, f, indent=2)
