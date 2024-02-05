import json
import decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0")
    }

    with open(file_name, "r") as file_trades:
        trades = json.load(file_trades)
        for trade in trades:
            if trade["bought"]:
                profit["matecoin_account"] += decimal.Decimal(trade["bought"])
                profit["earned_money"] -= (
                    decimal.Decimal(trade["bought"])
                    * decimal.Decimal(trade["matecoin_price"])
                )
            if trade["sold"]:
                profit["matecoin_account"] -= decimal.Decimal(trade["sold"])
                profit["earned_money"] += (
                    decimal.Decimal(trade["sold"])
                    * decimal.Decimal(trade["matecoin_price"])
                )

    profit["matecoin_account"] = str(profit.get("matecoin_account"))
    profit["earned_money"] = str(profit.get("earned_money"))
    with open("profit.json", "w") as file_profit:
        json.dump(profit, file_profit, indent=2)
