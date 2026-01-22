import decimal

import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f_load:
        trades_data = json.load(f_load)

    earned_money, matecoin_account = decimal.Decimal("0"), decimal.Decimal("0")

    for trade in trades_data:

        if trade["bought"] is not None:
            earned_money -= (decimal.Decimal(
                trade["bought"]) * decimal.Decimal(
                trade["matecoin_price"]))
            matecoin_account += decimal.Decimal(trade["bought"])

        if trade["sold"] is not None:
            earned_money += (decimal.Decimal(
                trade["sold"]) * decimal.Decimal(
                trade["matecoin_price"]))
            matecoin_account -= decimal.Decimal(trade["sold"])

    trades = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f_save:
        json.dump(trades, f_save, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
