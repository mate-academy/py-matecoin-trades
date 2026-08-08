import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file_trades:
        file_data = json.load(file_trades)

    money = 0
    matecoin_acc = 0

    for operation in file_data:
        if operation["bought"] is not None:
            matecoin_acc += decimal.Decimal(operation["bought"])
            money -= decimal.Decimal(operation["bought"]) * decimal.Decimal(
                operation["matecoin_price"]
            )
        if operation["sold"] is not None:
            matecoin_acc -= decimal.Decimal(operation["sold"])
            money += decimal.Decimal(operation["sold"]) * decimal.Decimal(
                operation["matecoin_price"]
            )

    calculate_profits = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin_acc),
    }

    with open("profit.json", "w") as file_profit:
        json.dump(calculate_profits, file_profit, indent=2)
