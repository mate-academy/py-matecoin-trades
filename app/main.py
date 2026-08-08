import json
from decimal import Decimal, getcontext


getcontext().prec = 28


def calculate_profit(filename: str) -> None:
    with open(filename) as json_file:
        data = json.load(json_file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for record in data:
        bought = record["bought"]
        sold = record["sold"]
        price = record["matecoin_price"]

        price_dec = Decimal(price)

        if bought is not None:
            bought_dec = Decimal(bought)
            matecoin_account += bought_dec
            earned_money -= bought_dec * price_dec

        if sold is not None:
            sold_dec = Decimal(sold)
            matecoin_account -= sold_dec
            earned_money += sold_dec * price_dec

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
