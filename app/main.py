import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)
    earned_money, matecoin_account = 0, 0

    for ele in data:
        if ele["bought"]:
            earned_money -= (decimal.Decimal(ele["bought"])
                             * decimal.Decimal(ele["matecoin_price"]))
            matecoin_account += decimal.Decimal(ele["bought"])

        if ele["sold"]:
            earned_money += (decimal.Decimal(ele["sold"])
                             * decimal.Decimal(ele["matecoin_price"]))
            matecoin_account -= decimal.Decimal(ele["sold"])

    earned_money = str(earned_money)
    matecoin_account = str(matecoin_account)
    account = {"earned_money": earned_money,
               "matecoin_account": matecoin_account}

    with open("profit.json", "w") as result:
        json.dump(account, result, indent=2)
