import json

from decimal import Decimal as Dec


def calculate_profit(name_of_file):
    with open(name_of_file, "r") as f:
        trades_info = json.load(f)

    print(trades_info)

    profit_info = {
        "earned_money": Dec("0"),
        "matecoin_account": Dec("0"),
    }

    for trade in trades_info:
        if trade["bought"]:
            profit_info["matecoin_account"] += Dec(trade["bought"])
            profit_info["earned_money"] -= (
                Dec(trade["bought"]) * Dec(trade["matecoin_price"])
            )
            continue
        if trade["sold"]:
            profit_info["matecoin_account"] -= Dec(trade["sold"])
            profit_info["earned_money"] += (
                Dec(trade["sold"]) * Dec(trade["matecoin_price"])
            )

    print(profit_info)

    with open("profit.json", "w") as f:
        for key in profit_info.keys():
            profit_info[key] = str(profit_info[key])
        json.dump(profit_info, f, indent=2)


if __name__ == '__main__':
    calculate_profit("trades.json")
