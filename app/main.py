import decimal
import json


def calculate_profit(filename):
    earned_money = decimal.Decimal("0.0")
    matecoin_account = decimal.Decimal("0.0")

    with open(filename, "r") as trades:
        deals_data = json.load(trades)
    for deal in deals_data:
        price = decimal.Decimal(deal["matecoin_price"])
        if deal["bought"] is not None:
            bought_amount = decimal.Decimal(deal["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * price
        if deal["sold"] is not None:
            sold_amount = decimal.Decimal(deal["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    with open("profit.json", "w") as profit:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  profit, indent=2)
