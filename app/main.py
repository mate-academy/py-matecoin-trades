import decimal
import json


def calculate_profit(file_name: str) -> None:
    total_coin = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")

    with open(file_name, "r") as open_file:
        trades_dict = json.load(open_file)

    for operation in trades_dict:
        price = decimal.Decimal(operation["matecoin_price"])

        if operation["bought"]:
            bought = decimal.Decimal(operation["bought"])
            total_coin += bought
            earned_money += bought * price

        if operation["sold"]:
            sold = decimal.Decimal(operation["sold"])
            total_coin -= sold
            earned_money -= sold * price

    with (open("profit.json", "w") as profit_file):
        result = {
            "earned_money": str(-earned_money),
            "matecoin_account": str(total_coin)
        }
        json.dump(result, profit_file, indent=2)
