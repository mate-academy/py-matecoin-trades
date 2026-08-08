import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with (open(filename, "r") as jsonfile):
        fil = json.load(jsonfile)
        profit = Decimal("0")
        matecoin_account = Decimal("0")
        for operation in fil:
            if operation["bought"] is not None:
                matecoin_account += Decimal(str(operation["bought"]))
                profit -= Decimal(str(operation["bought"]
                                      )) * Decimal(
                    str(operation["matecoin_price"]))
            if operation["sold"] is not None:
                matecoin_account -= Decimal(str(operation["sold"]))
                profit += Decimal(str(operation["sold"]
                                      )) * Decimal(
                    str(operation["matecoin_price"]))
    result = {"earned_money": str(profit),
              "matecoin_account": str(matecoin_account)}
    print(result)
    with open("profit.json", "w") as pj:
        json.dump(result, pj, indent=2)
