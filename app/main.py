import json
from decimal import Decimal


def calculate_profit(name: str) -> None:

    with open(name) as f:
        datas = json.load(f)

    out = {}
    sum_price_bought = Decimal()
    sum_bought = Decimal()
    sum_price_sold = Decimal()
    sum_sold = Decimal()

    for data in datas:
        dec_matecoin_price = Decimal(data["matecoin_price"])

        if data["bought"]:
            dec_bought = Decimal(data["bought"])
            sum_price_bought += dec_bought * dec_matecoin_price
            sum_bought += dec_bought

        if data["sold"]:
            dec_sold = Decimal(data["sold"])
            sum_price_sold += dec_sold * dec_matecoin_price
            sum_sold += dec_sold

    out["earned_money"] = str(sum_price_sold - sum_price_bought)
    out["matecoin_account"] = str(sum_bought - sum_sold)

    with open("profit.json", "wt") as f:
        json.dump(out, f, indent=2)

