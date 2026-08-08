import decimal
import json


def calculate_profit(name: str) -> None:
    with open(name, "r") as f:
        all_trades = json.load(f)

    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)

    for trade in all_trades:
        if isinstance(trade["bought"], str):
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["bought"]))
        if isinstance(trade["sold"], str):
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["sold"]))

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
