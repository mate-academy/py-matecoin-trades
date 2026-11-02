from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    if not transactions:
        return

    account = 0
    profit = 0

    for transaction in transactions:
        units_bought, units_sold, price = transaction.values()

        precise_price = Decimal(str(price))

        if units_bought:
            precise_bought = Decimal(str(units_bought))
            profit -= precise_bought * precise_price
            account += precise_bought
        if units_sold:
            precise_sold = Decimal(str(units_sold))
            profit += precise_sold * precise_price
            account -= precise_sold

    with open("profit.json", "w") as file:
        json.dump({"earned_money": str(profit),
                   "matecoin_account": str(account)},
                  file, indent=2)
