import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r+") as file:
        coins_info = json.load(file)

    coins_bought = 0
    coins_sold = 0
    profit_or_loss = 0
    for operation in coins_info:
        bought = Decimal(operation["bought"]) if operation["bought"] else 0
        coins_bought += bought
        sold = Decimal(operation["sold"]) if operation["sold"] else 0
        coins_sold += sold
        coin_price = Decimal(operation["matecoin_price"])
        profit_or_loss += (sold * coin_price) - (bought * coin_price)
    acc = coins_bought - coins_sold
    profit = {
        "earned_money": str(profit_or_loss),
        "matecoin_account": str(acc),
    }
    with open("profit.json", "w") as fl:
        json.dump(profit, fl, indent=2)
