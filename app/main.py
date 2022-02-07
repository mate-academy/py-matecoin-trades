import json
import decimal


def calculate_profit(file_name):
    with open(file_name) as json_file:
        trades = json.load(json_file)

        earned_money = 0
        matecoin_account = 0

        for trade in trades:
            if trade["bought"] is not None and trade["sold"] is None:
                earned_money -= decimal.Decimal(trade["bought"]) * \
                                decimal.Decimal(trade["matecoin_price"])
                matecoin_account -= decimal.Decimal(trade["bought"])
            if trade["bought"] is None and trade["sold"] is not None:
                earned_money += decimal.Decimal(trade["sold"]) * \
                                decimal.Decimal(trade["matecoin_price"])
                matecoin_account += decimal.Decimal(trade["sold"])

        profit_data = {
            "earned_money": f"{earned_money}",
            "matecoin_account": f"{matecoin_account}"
        }

        with open("profit.json", "w") as file_profit:
            json.dump(profit_data, file_profit, indent=2)


calculate_profit("trades.json")
