import json
import decimal


def calculate_profit(file_name):
    with open(file_name) as json_file:
        trades = json.load(json_file)

        earned_money = 0
        matecoin_amount = 0

        for trade in trades:
            price = decimal.Decimal(trade["matecoin_price"])
            if trade["bought"]:
                earned_money -= decimal.Decimal(trade["bought"]) * price
                matecoin_amount += decimal.Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += decimal.Decimal(trade["sold"]) * price
                matecoin_amount -= decimal.Decimal(trade["sold"])

        data_of_amount = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_amount)
        }

        with open("profit.json", "w") as file_ammount:
            json.dump(data_of_amount, file_ammount, indent=2)


calculate_profit("trades.json")
