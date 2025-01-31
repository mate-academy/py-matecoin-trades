import json
import decimal


def calculate_profit(trades: json) -> None:
    with open(trades) as d:
        trades_data = json.load(d)

    earned_money = 0
    matecoin_account = 0

    for trade in trades_data:
        if trade["bought"] is not None:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -=\
                (decimal.Decimal(trade["bought"])
                 * decimal.Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += \
                (decimal.Decimal(trade["sold"])
                 * decimal.Decimal(trade["matecoin_price"]))

    trades_profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as d:
        json.dump(trades_profit, d, indent=2)
