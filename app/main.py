import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades_data = json.load(file)
    wallet = Decimal("0")
    earned = Decimal("0")
    for data in trades_data:
        bought = Decimal("0")
        sold = Decimal("0")
        current_price = Decimal(data["matecoin_price"])
        if data["bought"]:
            bought = Decimal(data["bought"])
        wallet += bought
        if data["sold"]:
            sold = Decimal(data["sold"])
        wallet -= sold
        earned -= current_price * bought
        earned += current_price * sold
    account_data = {
        "earned_money": str(earned),
        "matecoin_account": str(wallet)
    }
    with open("profit.json", "w") as report:
        json.dump(account_data, report, indent=2)
