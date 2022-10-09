import json
import decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as f,
          open("profit.json", "w") as profit_file):
        trades = json.load(f)

        profit = {"earned_money": decimal.Decimal("0"),
                  "matecoin_account": decimal.Decimal("0")}
        for trade in trades:
            if isinstance(trade["bought"], str):
                profit["earned_money"] -= (decimal.Decimal(trade["bought"]) *
                                           decimal.Decimal(trade["matecoin_price"]))
                profit["matecoin_account"] += decimal.Decimal(trade["bought"])
            if isinstance(trade["sold"], str):
                profit["earned_money"] += (decimal.Decimal(trade["sold"]) *
                                           decimal.Decimal(trade["matecoin_price"]))
                profit["matecoin_account"] -= decimal.Decimal(trade["sold"])
        profit["earned_money"] = str(profit["earned_money"])
        profit["matecoin_account"] = str(profit["matecoin_account"])
        print(profit)
        json.dump(profit, profit_file, indent=2)
