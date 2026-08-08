import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (
        open(file_name, "r") as data_file,
        open("profit.json", "w") as profit_file
    ):
        coin_data = json.load(data_file)
        earned_money = 0
        mate_acc = 0
        for i in coin_data:
            if i["bought"] is not None:
                earned_money -= (
                    Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                )
                mate_acc += Decimal(i["bought"])
            if i["sold"] is not None:
                earned_money += (
                    Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                )
                mate_acc -= Decimal(i["sold"])
        res = {
            "earned_money": str(earned_money),
            "matecoin_account": str(mate_acc)
        }

        json.dump(res, profit_file, indent=2)
