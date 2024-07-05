from decimal import Decimal
import json


def calculate_profit(file_name: str):
    data_file = []
    with open (file_name, "r", encoding="utf-8") as file:
        data_file = json.load(file)

    earned_money = Decimal(value="0")
    matecoin_account = Decimal(value=0)
    for item in data_file:
        if item["bought"]:
            bought_volume = Decimal(item["bought"])
            bought_price = Decimal(item["matecoin_price"])
            cost = bought_volume * bought_price
            matecoin_account += bought_volume
            earned_money -= cost
        if item["sold"]:
            sold_volume = Decimal(item["sold"])
            sold_price = Decimal(item["matecoin_price"])
            income = sold_volume * sold_price
            matecoin_account -= sold_volume
            earned_money += income

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)
