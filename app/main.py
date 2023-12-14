import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    bought_amount = decimal.Decimal("0")
    sold_amount = decimal.Decimal("0")
    bought = decimal.Decimal("0")
    sold = decimal.Decimal("0")

    for operation in trades:
        if operation["bought"]:
            bought_amount += (decimal.Decimal(operation["bought"])
                              * decimal.Decimal(operation["matecoin_price"]))
            bought += decimal.Decimal(operation["bought"])
        if operation["sold"]:
            sold_amount += (decimal.Decimal(operation["sold"])
                            * decimal.Decimal(operation["matecoin_price"]))
            sold += decimal.Decimal(operation["sold"])
    earned_money = sold_amount - bought_amount
    matecoin_account = bought - sold
    print(earned_money)
    print(matecoin_account)

    with open("profit.json", "w") as file:
        res = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(res, file, indent=2)
