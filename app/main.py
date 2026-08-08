import decimal
import json


def calculate_profit(source_file: str) -> None:
    with open(source_file, "r") as read_file:
        trades = json.load(read_file)

    earned_money = matecoin_account = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            earned_money -= (decimal.Decimal(trade["bought"])
                             * decimal.Decimal(trade["matecoin_price"]))
            matecoin_account += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (decimal.Decimal(trade["sold"])
                             * decimal.Decimal(trade["matecoin_price"]))
            matecoin_account -= decimal.Decimal(trade["sold"])

    with open("profit.json", "w") as write_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            write_file,
            indent=2
        )
