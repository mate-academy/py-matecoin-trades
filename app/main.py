import json
import decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": decimal.Decimal(0),
        "matecoin_account": decimal.Decimal(0)
    }
    with open(file_name) as file:
        trades_operations = json.load(file)
        for operation in trades_operations:
            matecoin_price = decimal.Decimal(operation["matecoin_price"])
            if operation["bought"] is not None:
                bought = decimal.Decimal(operation["bought"])
                profit["earned_money"] -= bought * matecoin_price
                profit["matecoin_account"] += bought
            if operation["sold"] is not None:
                sold = decimal.Decimal(operation["sold"])
                profit["earned_money"] += sold * matecoin_price
                profit["matecoin_account"] -= sold

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
