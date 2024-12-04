import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
        counter = 0
        balans = 0
        for trade in trades:
            if trade["bought"] is None:
                trade["bought"] = 0
            if trade["sold"] is None:
                trade["sold"] = 0

            dec_sold = Decimal(trade["sold"])
            dec_bought = Decimal(trade["bought"])
            dec_price = Decimal(trade["matecoin_price"])
            costs = dec_bought * dec_price
            gains = dec_sold * dec_price

            counter += gains - costs
            balans += dec_bought - dec_sold
        counter_str = str(counter)
        balans_str = str(balans)
        results = {"earned_money": counter_str, "matecoin_account": balans_str}
        with open("profit.json", "w") as new_file:
            json.dump(results, new_file, indent=2)
