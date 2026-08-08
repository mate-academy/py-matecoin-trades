import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

        earned_money = 0
        matecoin_account = 0
        for trade in trades:
            if trade["bought"]:
                earned_money -= (decimal.Decimal(trade["bought"])
                                 * decimal.Decimal(trade["matecoin_price"]))
                matecoin_account += decimal.Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += (decimal.Decimal(trade["sold"])
                                 * decimal.Decimal(trade["matecoin_price"]))
                matecoin_account -= decimal.Decimal(trade["sold"])

    data_file = {"earned_money": str(earned_money),
                 "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f:
        json.dump(data_file, f, indent=2)
