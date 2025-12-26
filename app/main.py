import json
from decimal import Decimal as dec


def calculate_profit(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
        earned_money = 0
        matecoin_account = 0
        for trade in data:
            if trade["bought"] is not None:
                coins = dec(trade["bought"])
                earned_money -= coins * dec(trade["matecoin_price"])
                matecoin_account += coins
            if trade["sold"] is not None:
                coins = dec(trade["sold"])
                earned_money += coins * dec(trade["matecoin_price"])
                matecoin_account -= coins
        result = {"earned_money": f"{earned_money}",
                  "matecoin_account": f"{matecoin_account}"
                  }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
