import json

from decimal import Decimal

def check__data(dict_key_for_test: str, dict_for_test: dict) -> bool:
    condition_1 = dict_key_for_test in dict_for_test
    condition_2 = dict_for_test[dict_key_for_test] is not None
    return all([condition_1, condition_2])



def collect_data(data_for_parsing: dict) -> Decimal:
    result = {}
    for dict_key in ("bought", "sold", "matecoin_price"):
        if check__data(dict_key, data_for_parsing):
            result[dict_key] = data_for_parsing[dict_key]


    if condition_1 and condition_2:
        return Decimal(data_for_parsing[dict_name])
    return Decimal(0)


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", newline="", encoding="utf-8") as f:
        dataset = json.load(f)
    earn_bought = Decimal(0)
    earn_sold = Decimal(0)
    average_matecoin_price = Decimal(0)
    count_iteration = Decimal(0)
    for dict_with_coin in dataset:
        count_iteration += 1
        earn_bought += check_and_collect_data("bought", dict_with_coin)
        earn_sold += check_and_collect_data("sold", dict_with_coin)
        average_matecoin_price += check_and_collect_data("matecoin_price", dict_with_coin)
    the_total_money = earn_bought + earn_sold
    the_average_price = average_matecoin_price / count_iteration

    with open("profit.json", "w", newline="", encoding="utf-8") as f:
        json.dump({"earned_money": f"{the_total_money}", "matecoin_account": f"{1 / the_average_price}"}, f, indent=2)

calculate_profit("t.json")
#,{"earned_money": "-4.4472448", "matecoin_account": "0.00009"},