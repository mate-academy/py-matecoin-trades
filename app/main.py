import json
from decimal import Decimal


def calculate_profit(name: str):
    with open(name) as f:
        data = json.load(f)
        money = Decimal("0")
        account = Decimal("0")
        for trans in data:
            if trans["bought"] is not None:
                money += Decimal(trans["bought"])
                mul1 = Decimal(trans["bought"])
                mul2 = Decimal(trans["matecoin_price"])
                account += mul1 * mul2

            if trans["sold"] is not None:
                money -= Decimal(trans["sold"])
                mul1 = Decimal(trans["sold"])
                mul2 = Decimal(trans["matecoin_price"])
                account -= mul1 * mul2

        profit = {
            "earned_money": str(money),
            "matecoin_account": str(account)
        }
        with open("profit.json", "w") as file:
            json.dump(profit, file, indent=2)


calculate_profit("trades.json")
