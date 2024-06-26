import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    earned_money = Decimal("0")
    for trade in trades:
        price = Decimal(f"{trade['matecoin_price']}")
        if trade["bought"]:
            total_bought += Decimal(f"{trade['bought']}")
            earned_money -= Decimal(f"{trade['bought']}") * price
        if trade["sold"]:
            total_sold += Decimal(f"{trade['sold']}")
            earned_money += Decimal(f"{trade['sold']}") * price
    account = total_bought - total_sold
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account)
    }

    print("PROFIT: ", profit)
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
