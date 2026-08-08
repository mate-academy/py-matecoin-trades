import json
import decimal


def calculate_profit(filename: str) -> None:
    profit = decimal.Decimal("0.0")
    balance = decimal.Decimal("0.0")
    with open(filename) as trades_file:
        trades = json.load(trades_file)
    for trade in trades:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            balance += bought
            profit -= bought * price

        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            balance -= sold
            profit += sold * price

    with open("profit.json", "w") as profit_file:
        json.dump({"earned_money": str(profit),
                   "matecoin_account": str(balance)}, profit_file,
                  indent=2)
