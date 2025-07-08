import json
import decimal


def calculate_profit(trades_file: str = "trades.json",
                     profit_file: str = "profit.json") -> None:

    with (open(trades_file, "r") as json_trades):
        trades = json.load(json_trades)
        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")
        for trade in trades:
            if trade["bought"] is not None:
                earned_money -= (
                    decimal.Decimal(trade["bought"])
                    * decimal.Decimal(trade["matecoin_price"])
                )
                matecoin_account += decimal.Decimal(trade["bought"])

            if trade["sold"] is not None:
                earned_money += (
                    decimal.Decimal(trade["sold"])
                    * decimal.Decimal(trade["matecoin_price"])
                )
                matecoin_account -= decimal.Decimal(trade["sold"])
    trades_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open(profit_file, "w") as json_profit:
        json.dump(trades_result, json_profit, indent=2)

    return None
