import json
import decimal


def calculate_profit(trades: list) -> None:
    with open("app/trades.json", "r") as read_file:
        data = json.load(read_file)

    earned_money = 0
    matecoin_account = 0

    for trade in data:
        if trade["bought"]:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= decimal.Decimal(trade["bought"]) \
                * decimal.Decimal(trade["matecoin_price"])
        if trade["sold"]:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += decimal.Decimal(trade["sold"]) \
                * decimal.Decimal(trade["matecoin_price"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as write_file:
        json.dump(profit, write_file, indent=2)
