import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as trades:
        trades_file = json.load(trades)
        profit = {"earned_money": decimal.Decimal("0"),
                  "matecoin_account": decimal.Decimal("0")}
        for transaction in trades_file:
            matecoin_price = decimal.Decimal(transaction["matecoin_price"])
            if transaction["bought"]:
                bought = decimal.Decimal(transaction["bought"])
                profit["matecoin_account"] += bought
                earned = bought * matecoin_price
                profit["earned_money"] -= earned
            if transaction["sold"]:
                sold = decimal.Decimal(transaction["sold"])
                profit["matecoin_account"] -= sold
                earned = sold * matecoin_price
                profit["earned_money"] += earned
        profit["matecoin_account"] = str(profit["matecoin_account"])
        profit["earned_money"] = str(profit["earned_money"])
        with open("profit.json", "w") as profit_file:
            json.dump(profit, profit_file, indent=2)
