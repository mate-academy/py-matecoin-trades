import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as file_input,
          open("profit.json", "w") as file_otput):
        data_in = json.load(file_input)
        earned_money = Decimal("0")
        account = Decimal("0")
        for trade in data_in:
            if trade["sold"]:
                sold = Decimal(trade["sold"])
                price = Decimal(trade["matecoin_price"])
                earned_money += sold * price
                account -= sold
            if trade["bought"]:
                bought = Decimal(trade["bought"])
                price = Decimal(trade["matecoin_price"])
                earned_money -= bought * price
                account += bought
        data_out = {
            "earned_money": str(earned_money),
            "matecoin_account": str(account)
        }
        json.dump(data_out, file_otput, indent=2)
