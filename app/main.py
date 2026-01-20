import decimal
import json


def calculate_profit(trades_file_name: str) -> None:

    with open(trades_file_name, "r") as file:
        trades_data = json.load(file)

    coins_amount = decimal.Decimal("0.0")
    money_spent = decimal.Decimal("0.0")
    money_received = decimal.Decimal("0.0")

    for trade in trades_data:
        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            money_spent += bought * matecoin_price
            coins_amount += bought
        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            money_received += sold * matecoin_price
            coins_amount -= sold

    profit = {
        "earned_money": str(money_received - money_spent),
        "matecoin_account": str(coins_amount)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
