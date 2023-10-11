import json
from decimal import Decimal


def calculate_profit(operating_file: json) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(operating_file) as f:
        read_file = json.load(f)

    for read in read_file:
        bought = read.get("bought")
        sold = read.get("sold")
        matecoin_price = Decimal(read["matecoin_price"])
        if bought:
            bought = Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold:
            sold = Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
