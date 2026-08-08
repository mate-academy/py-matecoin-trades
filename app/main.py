import json
import decimal


def calculate_profit(file_name: str) -> None:
    profit = {"earned_money": decimal.Decimal("0"),
              "matecoin_account": decimal.Decimal("0")}
    with open(file_name, "r") as file:
        data = json.load(file)
        for trade in data:
            price = decimal.Decimal(trade["matecoin_price"])
            if trade["bought"]:
                bought = decimal.Decimal(trade["bought"])
                profit["matecoin_account"] += bought
                profit["earned_money"] -= bought * price
            if trade["sold"]:
                sold = decimal.Decimal(trade["sold"])
                profit["matecoin_account"] -= sold
                profit["earned_money"] += sold * price

        with open("profit.json", "w") as f:
            json.dump({key: str(value)
                       for key, value in profit.items()}, f, indent=2)
