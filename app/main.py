import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as file:
        transactions = json.load(file)

    profit = Decimal("0.0")
    account_funds = Decimal("0.0")

    for trade in transactions:
        if trade["bought"]:
            bought, price = trade.get("bought"), trade.get("matecoin_price")
            profit -= Decimal(bought) * Decimal(price)
            account_funds += Decimal(bought)

        if trade["sold"]:
            sold, price = trade.get("sold"), trade.get("matecoin_price")
            profit += Decimal(sold) * Decimal(price)
            account_funds -= Decimal(sold)

    upload_data = {
        "earned_money": str(profit),
        "matecoin_account": str(account_funds)}

    with open("profit.json", "w") as file:
        json.dump(upload_data, file, indent=2)
