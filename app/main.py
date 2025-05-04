import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as file:
        matecoin_currency = json.load(file)
        money = Decimal("0")
        matecoin = Decimal("0")
        for transaction in matecoin_currency:
            price = Decimal(transaction["matecoin_price"])
            if transaction["sold"] is not None:
                sold = Decimal(transaction["sold"])
                money += sold * price
                matecoin -= sold
            if transaction["bought"] is not None:
                bought = Decimal(transaction["bought"])
                money -= bought * price
                matecoin += bought

    account = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as f:
        json.dump(account, f, indent=2)
