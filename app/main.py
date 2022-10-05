import decimal
import json


def calculate_profit(trade: str) -> None:
    with open(trade) as f:
        trades = json.load(f)

    earned_money = 0
    mate_coin_account = 0

    for trade in trades:
        mate_coin_price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            earned_money -= mate_coin_price * bought
            mate_coin_account += bought

        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            earned_money += mate_coin_price * sold
            mate_coin_account -= sold

    user = {
        "earned_money": str(earned_money),
        "matecoin_account": str(mate_coin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(user, f, indent=2)

    return None
