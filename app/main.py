import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as json_file:
        data = json.load(json_file)
        print(data)
        profit = 0
        account = 0
        for operation in data:
            if operation.get("sold") is None:
                profit -= Decimal(operation["bought"]) * Decimal(operation["matecoin_price"])
                account += Decimal(operation["bought"])
            else:
                profit += Decimal(operation["sold"]) * Decimal(operation["matecoin_price"])
                account -= Decimal(operation["sold"])

    with open("profit.json", "w") as json_target:
        json.dump({
            "earned_money": str(profit),
            "matecoin_account": str(account)
        }, json_target)


if __name__ == "__main__":
    print(calculate_profit("app/trades.json"))




