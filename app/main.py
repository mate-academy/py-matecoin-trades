import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as f:
        trades_data = json.load(f)
    profit = 0
    account = 0
    for operation in trades_data:
        if operation["bought"] is not None:
            calc = Decimal(operation["bought"]) * Decimal(operation["matecoin_price"])
            profit += calc
            account += Decimal(operation["bought"])
        else:
            calc = Decimal(operation["sold"]) * Decimal(operation["matecoin_price"])
            profit -= calc
            account -= Decimal(operation["sold"])
    prof = [{
      "earned_money": str(profit),
      "matecoin_account": str(account)
    }]
    with open("profit.json", "w") as f:
        json.dump(prof, f, indent=2)
