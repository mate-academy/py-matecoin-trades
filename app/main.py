import json


def calculate_profit():
    profit = {"earned_money": 0,
              "matecoin_account": 0}
    with open("trades.json") as f:
        data = json.load(f)
        for new_dict in data:
            if new_dict["bought"] != 'null':
                profit["matecoin_account"] += new_dict["bought"]
                profit["earned_money"] -= new_dict["bought"] *\
                    new_dict["matecoin_price"]
            if new_dict["sold"] != 'null':
                profit["matecoin_account"] -= \
                    new_dict["sold"]
                profit["earned_money"] += new_dict["sold"] *\
                    new_dict["matecoin_price"]
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
