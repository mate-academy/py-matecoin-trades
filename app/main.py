import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as json_data:
        trade_data = json.load(json_data)
    count_money = Decimal(0)
    count_matecion = Decimal(0)
    for data_dict in trade_data:
        matecoin_price = Decimal(data_dict["matecoin_price"])
        if data_dict["bought"]:
            bought = Decimal(data_dict["bought"])
            count_money -= bought * matecoin_price
            count_matecion += bought
        if data_dict["sold"]:
            sold = Decimal(data_dict["sold"])
            count_money += sold * matecoin_price
            count_matecion -= sold
    result_dict = {
        "earned_money": str(count_money),
        "matecoin_account": str(count_matecion)
    }
    with open("profit.json", "w") as result_file:
        json.dump(result_dict, result_file, indent=2)
