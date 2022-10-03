from decimal import Decimal
import json


def calculate_profit(file_name):
    money_earned = 0
    matecoins = 0
    with open(file_name) as f:
        trading = json.load(f)
    for trade in trading:
        price = Decimal(trade['matecoin_price'])
        if trade["bought"]:
            money_earned -= Decimal(trade["bought"]) * price
            matecoins += Decimal(trade["bought"])
        if trade["sold"]:
            money_earned += Decimal(trade["sold"]) * price
            matecoins -= Decimal(trade["sold"])
    result = {
        "earned_money": f"{money_earned}",
        "matecoin_account": f"{matecoins}"
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
