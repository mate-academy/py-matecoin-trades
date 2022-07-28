import json
from decimal import Decimal


def calculate_profit(name_of_the_file: str):
    with open(name_of_the_file, "r") as f:
        trades = json.load(f)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for operation in trades:
            if operation["bought"] is not None:
                earned_money -= \
                    Decimal(operation["bought"]) \
                    * Decimal(operation["matecoin_price"])
                matecoin_account +=\
                    Decimal(operation["bought"])
            if operation["sold"] is not None:
                earned_money +=\
                    Decimal(operation["sold"]) \
                    * Decimal(operation["matecoin_price"])
                matecoin_account -= Decimal(operation["sold"])
        profit =\
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }
        with open("profit.json", "w") as f_w:
            json.dump(profit, f_w, indent=2)
