import json

from decimal import Decimal


def calculate_profit(json_file_name: str) -> None:
    with open(json_file_name) as file1:
        python_list = json.load(file1)
        profit_dict = {"earned_money": "0", "matecoin_account": "0"}
        sum_profit = Decimal("0")
        sum_matecoin = Decimal("0")
    for day_dict in python_list:
        day_bought = Decimal(day_dict.get("bought")) \
            if day_dict.get("bought") is not None else Decimal("0")
        day_sold = Decimal(day_dict.get("sold")) \
            if day_dict.get("sold") is not None else Decimal("0")
        day_price = Decimal(day_dict.get("matecoin_price"))
        sum_profit += (day_sold - day_bought) * day_price
        sum_matecoin += (day_bought - day_sold)
    profit_dict["earned_money"] = str(sum_profit)
    profit_dict["matecoin_account"] = str(sum_matecoin)
    with open("profit.json", "w") as file2:
        json.dump(profit_dict, file2, indent=2)
