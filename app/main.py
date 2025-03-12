import json
import decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        trades = json.load(file)

        earned_money = decimal.Decimal(0)
        matecoin_account = decimal.Decimal(0)

        for trade in trades:
            if trade["bought"]:
                earned_money -= decimal.Decimal(
                    trade["bought"]
                ) * decimal.Decimal(trade["matecoin_price"])
                matecoin_account += decimal.Decimal(trade["bought"])

            elif trade["sold"]:
                earned_money += decimal.Decimal(
                    trade["sold"]
                ) * decimal.Decimal(trade["matecoin_price"])
                matecoin_account -= decimal.Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=4)
