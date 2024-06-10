import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        bought = (Decimal(trade["bought"])
                  if trade["bought"] is not None
                  else Decimal("0"))
        sold = (Decimal(trade["sold"])
                if trade["sold"] is not None
                else Decimal("0"))
        matecoin_price = Decimal(trade["matecoin_price"])
        matecoin_account += bought - sold
        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
