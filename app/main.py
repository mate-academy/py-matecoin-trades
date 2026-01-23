import decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as trades_r:
        trades = json.load(trades_r)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            cost = (decimal.Decimal(trade["bought"])
                    * decimal.Decimal(trade["matecoin_price"]))
            earned_money -= cost
            matecoin_account += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            revenue = (decimal.Decimal(trade["sold"])
                       * decimal.Decimal(trade["matecoin_price"]))
            earned_money += revenue
            matecoin_account -= decimal.Decimal(trade["sold"])

    with open("profit.json", "w") as f:
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(result, f, indent=2)
