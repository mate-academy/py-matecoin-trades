import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    with open(filename, "r") as infile:
        trades = json.load(infile)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            earned_money -= Decimal(str(trade["bought"])) \
                * Decimal(str(trade["matecoin_price"]))
            matecoin_account += Decimal(str(trade["bought"]))
        if trade["sold"] is not None:
            earned_money += Decimal(str(trade["sold"])) \
                * Decimal(str(trade["matecoin_price"]))
            matecoin_account -= Decimal(str(trade["sold"]))

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2, sort_keys=True)
        outfile.write("\n")


if __name__ == "__main__":
    calculate_profit("trades.json")
