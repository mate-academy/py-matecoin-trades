import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades:
        transactions = json.load(trades)

    dollars_wallet = Decimal("0")
    coins_wallet = Decimal("0")
    for transaction in transactions:
        token_price = transaction["matecoin_price"]
        if count_bought_coins := transaction["bought"]:
            dollars_wallet -= (Decimal(count_bought_coins)
                               * Decimal(token_price))
            coins_wallet += Decimal(count_bought_coins)
        if count_sold_coins := transaction["sold"]:
            dollars_wallet += Decimal(count_sold_coins) * Decimal(token_price)
            coins_wallet -= Decimal(count_sold_coins)
    account = {
        "earned_money": str(dollars_wallet),
        "matecoin_account": str(coins_wallet)
    }

    with open("profit.json", "w") as profit:
        json.dump(account, profit, indent=2)
