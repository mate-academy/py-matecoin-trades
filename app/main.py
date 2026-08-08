import json
import decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(file_name) as f:
        operations = json.load(f)

    for operation in operations:
        if operation["bought"]:
            matecoin_account += decimal.Decimal(operation["bought"])
            earned_money -= decimal.Decimal(
                operation["matecoin_price"]
            ) * decimal.Decimal(operation["bought"])
        if operation["sold"]:
            matecoin_account -= decimal.Decimal(operation["sold"])
            earned_money += decimal.Decimal(
                operation["matecoin_price"]
            ) * decimal.Decimal(operation["sold"])

    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            f,
            indent=2,
        )
