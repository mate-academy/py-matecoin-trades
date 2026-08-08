import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_read:
        data = json.load(file_read)
    earned_money = 0
    matecoin_account = 0
    for tran in data:
        if tran["bought"]:
            matecoin_account += decimal.Decimal(tran["bought"])
            earned_money -= (decimal.Decimal(tran["bought"])
                             * decimal.Decimal(tran["matecoin_price"]))
        if tran["sold"]:
            matecoin_account -= decimal.Decimal(tran["sold"])
            earned_money += (decimal.Decimal(tran["sold"])
                             * decimal.Decimal(tran["matecoin_price"]))
    with open("profit.json", "w") as profit:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit, indent=2
        )
