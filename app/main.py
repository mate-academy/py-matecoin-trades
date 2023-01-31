import json

from _decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    bought = 0
    sold = 0
    matecoin_account = 0
    with open(name_of_file, "r") as file:
        data = json.load(file)

        for i in data:
            if i["bought"]:
                bought += (Decimal(i["bought"]) * Decimal(i["matecoin_price"]))
                matecoin_account += Decimal(i["bought"])
            if i["sold"]:
                sold += (Decimal(i["sold"]) * Decimal(i["matecoin_price"]))
                matecoin_account -= Decimal(i["sold"])
    profit = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(matecoin_account)
    }

    path = "C:/Mate/py-matecoin-trades/" + "profit.json"
    with open(path, "w") as file:
        json.dump(profit, file, indent=2)
