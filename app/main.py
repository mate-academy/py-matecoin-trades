import json
import decimal


def calculate_profit(file_name):

    earned_money = 0
    matecoin_account = 0

    with open(file_name, "r") as json_data:
        data = json.load(json_data)

        for trade in data:
            if not trade["bought"]:
                trade["bought"] = 0
            if not trade["sold"]:
                trade["sold"] = 0

            earned_money +=\
                (decimal.Decimal(trade["bought"])
                 - decimal.Decimal(trade["sold"])) \
                * decimal.Decimal(trade["matecoin_price"])

            matecoin_account += (decimal.Decimal(trade["bought"])
                                 - decimal.Decimal(trade["sold"]))

    profit_dict = {"earned_money": f"{earned_money}",
                   "matecoin_account": f"{matecoin_account}"}

    with open("profit.json", "w") as profit:
        json.dump(profit_dict, profit, indent=2)


calculate_profit("trades.json")
