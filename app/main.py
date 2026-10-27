import json
from decimal import Decimal


def calculate_profit(trades_json):
    with open(trades_json, "r") as file:
        dictionary_with_trades = json.load(file)

    matecoin_account = Decimal(0)
    earnings = Decimal(0)

    for dictionary in dictionary_with_trades:
        price = Decimal(dictionary["matecoin_price"])
        if dictionary["bought"] is not None:
            bought = Decimal(dictionary["bought"])
            buy_money_spent = price * bought
            matecoin_account += bought
            earnings -= buy_money_spent

        if dictionary["sold"] is not None:
            sold = Decimal(dictionary["sold"])
            sell_money_spent = price * sold
            matecoin_account -= sold
            earnings += sell_money_spent

    result = {
        "earned_money": str(earnings),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
