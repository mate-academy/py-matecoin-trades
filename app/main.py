import json

import decimal


def calculate_profit(trades_json: json) -> json:
    with open(trades_json) as file:
        trades = json.load(file)

    buy = 0
    sell = 0
    account = 0
    for day in trades:
        if day["bought"]:
            price = day["matecoin_price"]
            bought = day["bought"]
            buy += decimal.Decimal(price) * decimal.Decimal(bought)
            account += decimal.Decimal(bought)

        if day["sold"]:
            price = day["matecoin_price"]
            sold = day["sold"]
            sell += decimal.Decimal(price) * decimal.Decimal(sold)
            account -= decimal.Decimal(sold)
    result_dict = {"earned_money": str(sell - buy),
                   "matecoin_account": str(account)}
    with open("profit.json", "w") as profit:
        json.dump(result_dict, profit, indent=2)
