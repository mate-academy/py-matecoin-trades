import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        data = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for transaction in data:
        if transaction.get("bought") is not None:
            matecoin_account += Decimal(transaction.get("bought"))
            earned_money -= Decimal(transaction.get("bought")) * \
                Decimal(transaction.get("matecoin_price"))
        if transaction.get("sold") is not None:
            matecoin_account -= Decimal(transaction.get("sold"))
            earned_money += Decimal(transaction.get("sold")) * \
                Decimal(transaction.get("matecoin_price"))
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)
              }
    print(profit)

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
