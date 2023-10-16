import decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    bought = sum(
        decimal.Decimal(i["bought"]) for i in data if i["bought"] is not None
    )
    sold = sum(
        decimal.Decimal(i["sold"]) for i in data if i["sold"] is not None
    )
    bought_matecoin = sum(
        decimal.Decimal(i["bought"]) * decimal.Decimal(i["matecoin_price"])
        for i in data if i["bought"] is not None
    )
    sold_matecoin = sum(
        decimal.Decimal(i["sold"]) * decimal.Decimal(i["matecoin_price"])
        for i in data if i["sold"] is not None
    )

    matecoin_account = bought - sold
    earned_money = sold_matecoin - bought_matecoin

    money = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(money, json_file, indent=2)
