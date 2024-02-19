import json
import decimal


def calculate_profit(filename: str) -> None:
    with (open(filename) as operations_file,
            open("../profit.json", "w") as result_file):
        operations = json.load(operations_file)
        spent_money, earned_money, mate_coins = 0, 0, 0
        for operation in operations:
            price = decimal.Decimal(operation["matecoin_price"])
            if operation["bought"]:
                spent_money += (decimal.Decimal(operation["bought"])
                                * price)
                mate_coins += decimal.Decimal(operation["bought"])
            if operation["sold"]:
                earned_money += (decimal.Decimal(operation["sold"])
                                 * price)
                mate_coins -= decimal.Decimal(operation["sold"])
        json.dump({
            "earned_money": str(earned_money - spent_money),
            "matecoin_account": str(mate_coins)
        }, result_file, indent=2)
