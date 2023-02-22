import json
from decimal import Decimal


def calculate_profit() -> None:
    with open("profit.json") as read_json_file:
        trades_info = json.load(read_json_file)

    profit = Decimal()
    account = Decimal()

    for trade in trades_info:

        bought = trade["bought"]
        sold = trade["sold"]
        price = trade["matecoin_price"]

        if bought:
            profit -= Decimal(bought) * Decimal(price)
            account += Decimal(bought)
        if sold:
            profit += Decimal(sold) * Decimal(price)
            account -= Decimal(sold)

    res = {"earned_money": str(profit), "matecoin_account": str(account)}
    print(res)
    with open("profit.json", "w") as write_json_file:
        json.dump(res, write_json_file, indent=2)
