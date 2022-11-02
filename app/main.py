import json
import decimal


def calculate_profit(trade: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(trade, "r") as file_in:
        data_trade = json.load(file_in)

    for trade in data_trade:
        if trade["bought"]:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= decimal.Decimal(trade["bought"])\
                * decimal.Decimal(trade["matecoin_price"])

        if trade["sold"]:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += decimal.Decimal(trade["sold"]) \
                * decimal.Decimal(trade["matecoin_price"])

    trade_result = {"earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file_out:
        json.dump(trade_result, file_out, indent=2)
