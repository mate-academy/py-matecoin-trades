import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)
    balance_of_coin = decimal.Decimal("0")
    amount = decimal.Decimal("0")
    for trade in trades:
        price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount -= decimal.Decimal(trade["bought"]) * price
            balance_of_coin += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            amount += decimal.Decimal(trade["sold"]) * price
            balance_of_coin -= decimal.Decimal(trade["sold"])
    profit = {"earned_money": str(amount),
              "matecoin_account": str(balance_of_coin)}
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
