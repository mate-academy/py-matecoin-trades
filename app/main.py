import json
import decimal


def calculate_profit():
    profit = {"earned_money": 0,
              "matecoin_account": 0}
    with open("trades.json") as json_file:
        data = json.load(json_file)
        for my_dic in data:
            if my_dic["bought"] != 'null':
                profit["matecoin_account"] += decimal.Decimal(my_dic["bought"])
                profit["earned_money"] -= decimal.Decimal(my_dic["bought"]) *\
                    decimal.Decimal(my_dic["matecoin_price"])
            if my_dic["sold"] != 'null':
                profit["matecoin_account"] -= \
                    decimal.Decimal(my_dic["sold"])
                profit["earned_money"] += decimal.Decimal(my_dic["sold"]) *\
                    decimal.Decimal(my_dic["matecoin_price"])
    with open("profit.json", "w") as new_json_file:
        json.dump(profit, new_json_file, indent=2)
