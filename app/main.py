import json
import decimal


def calculate_profit(json_file: str) -> None:
    dec = decimal.Decimal
    earned_money = dec("0.0")
    matecoin_account = dec("0.0")
    with open(json_file, "r") as file:
        trades = json.load(file)
        for trade in trades:
            if trade["bought"]:
                earned_money -= dec(
                    trade["bought"]) * dec(
                    trade["matecoin_price"])
                matecoin_account += dec(trade["bought"])
            if trade["sold"]:
                earned_money += dec(
                    trade["sold"]) * dec(
                    trade["matecoin_price"])
                matecoin_account -= dec(trade["sold"])

    with open("profit.json", "w") as file:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            file, indent=2
        )
