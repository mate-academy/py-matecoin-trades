import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)
    for trade in trades:
        if trade["sold"] is None:
            earned_money -= decimal.Decimal(trade["bought"]) * decimal.Decimal(
                trade["matecoin_price"]
            )
            matecoin_account += decimal.Decimal(trade["bought"])

        elif trade["bought"] is None:
            earned_money += decimal.Decimal(trade["sold"]) * decimal.Decimal(
                trade["matecoin_price"]
            )
            matecoin_account -= decimal.Decimal(trade["sold"])

        elif trade["sold"] is not None and trade["bought"] is not None:
            earned_money += (
                decimal.Decimal(trade["sold"])
                - decimal.Decimal(trade["bought"])
            ) * decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(
                trade["bought"]
            ) - decimal.Decimal(trade["sold"])

    with open("profit.json", "a") as file:
        json.dump(
            {
                "earned_money": f"{earned_money}",
                "matecoin_account": f"{matecoin_account}",
            },
            file,
            indent=2,
        )
