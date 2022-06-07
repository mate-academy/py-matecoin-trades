import json
from decimal import Decimal


def calculate_profit(name: str):
    with open(name) as f:
        data = json.load(f)
        bought = 0
        sold = 0
        bought_account = 0
        sold_account = 0
        for trans in data:
            if trans["bought"] is not None:
                bought += Decimal(trans["bought"])
                bought_account += \
                    Decimal(trans["bought"]) * \
                    Decimal(trans["matecoin_price"])
            bought += 0

            if trans["sold"] is not None:
                sold += Decimal(trans["sold"])
                sold_account += \
                    Decimal(trans["sold"]) * \
                    Decimal(trans["matecoin_price"])
            sold += 0

            money = bought - sold
            account = bought_account - sold_account

        profit = {
            "earned_money": str(money),
            "matecoin_account": str(account)
        }
        with open("profit.json", "w") as file:
            json.dump(profit, file, indent=2)


calculate_profit("trades.json")
