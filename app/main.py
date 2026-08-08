import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        trades = json.load(f)

    coins = decimal.Decimal(0)
    profit = decimal.Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            price = decimal.Decimal(trade["matecoin_price"])
            coins += bought
            profit -= bought * price

        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            price = decimal.Decimal(trade["matecoin_price"])
            profit += sold * price
            coins -= sold

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(coins)
    }
    with open("profit.json", "w") as json_prof:

        json.dump(result, json_prof, indent=2)
