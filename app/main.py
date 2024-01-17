import json
import decimal


def calculate_profit(json_f: str) -> None:
    with open(json_f) as f:
        trades_operations = json.load(f)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for operation in trades_operations:
        if operation["bought"] is not None:
            matecoin_account += decimal.Decimal(operation["bought"])
            earned_money -= (decimal.Decimal(operation["bought"])
                             * decimal.Decimal(operation["matecoin_price"]))
        if operation["sold"] is not None:
            matecoin_account -= decimal.Decimal(operation["sold"])
            earned_money += (decimal.Decimal(operation["sold"])
                             * decimal.Decimal(operation["matecoin_price"]))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
