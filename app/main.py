import json
import decimal


def calculate_profit(file_name: str) -> None:
    earned_money = decimal.Decimal(0.0)
    matecoin_account = decimal.Decimal(0.0)
    with open(file_name, "r") as file_in:
        all_trades = json.load(file_in)

    for trade in all_trades:
        if trade["bought"]:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["bought"]))
        if trade["sold"]:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["sold"]))

    with open("profit.json", "w") as file_out:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }
            , file_out
            , indent=2
        )
