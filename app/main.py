import decimal
import json


def calculate_profit(archive: str):
    with open(archive, "r") as f:
        trades = json.load(f)
    bought_balance = []
    sold_balance = []
    matecoin_balance = 0
    for operation in trades:
        if operation["bought"] is not None:
            bought_balance.append(
                decimal.Decimal(operation["bought"])
                * decimal.Decimal(operation["matecoin_price"])
            )
            matecoin_balance += decimal.Decimal(operation["bought"])
        if operation["sold"] is not None:
            sold_balance.append(
                decimal.Decimal(operation["sold"])
                * decimal.Decimal(operation["matecoin_price"])
            )
            matecoin_balance -= decimal.Decimal(operation["sold"])

    profit = sum(sold_balance) - sum(bought_balance)
    result = ({"earned_money": str(profit),
               "matecoin_account": str(matecoin_balance)})

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
