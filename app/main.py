import json
import decimal


def calculate_profit(file_name: str) -> None:
    profit = {"earned_money": 0,
              "matecoin_account": 0}

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(file_name, "r") as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"]:
            earned_money -= decimal.Decimal(
                trade["bought"]) * decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += decimal.Decimal(
                trade["sold"]) * decimal.Decimal(trade["matecoin_price"])
            matecoin_account -= decimal.Decimal(trade["sold"])

    profit["earned_money"] = str(earned_money)
    profit["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
