import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}", "r") as f:
        info = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for item in info:
        price = Decimal(item["matecoin_price"])
        if item["bought"] is not None:
            bought = Decimal(item["bought"])
            earned_money -= bought * price
            matecoin_account += bought
        if item["sold"] is not None:
            sold = Decimal(item["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": f"{earned_money: .7f}",
        "matecoin_account": f"{matecoin_account: .5f}"
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)

# calculate_profit("trades.json")
