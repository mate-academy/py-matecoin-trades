import decimal
import json


def calculate_profit(trades_file: str) -> None:

    trades = json.load(open(trades_file))

    data_profit = [0, 0]

    for trade in trades:
        if isinstance(trade["bought"], str):
            data_profit[0] -= (decimal.Decimal(trade["bought"]) *
                               decimal.Decimal(trade["matecoin_price"]))
            data_profit[1] += decimal.Decimal(trade["bought"])

        if isinstance(trade["sold"], str):
            data_profit[0] += (decimal.Decimal(trade["sold"]) *
                               decimal.Decimal(trade["matecoin_price"]))
            data_profit[1] -= decimal.Decimal(trade["sold"])

    for_dump_dict = {
        "earned_money": str(data_profit[0]),
        "matecoin_account": str(data_profit[1])
    }
    with open("profit.json", "w") as f:
        json.dump(for_dump_dict, f, indent=2)
