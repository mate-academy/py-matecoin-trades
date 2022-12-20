import json
import decimal


def calculate_profit(trade_file: str) -> None:
    profit = {
        "earned_money": decimal.Decimal(0),
        "matecoin_account": decimal.Decimal(0)
    }
    with open(trade_file, "r") as f:
        trades = json.load(f)
    for i in trades:
        if i["sold"]:
            profit["earned_money"] += decimal.Decimal(i["sold"]) * decimal.Decimal(i["matecoin_price"])
            profit["matecoin_account"] -= decimal.Decimal(i["sold"])
        if i["bought"]:
            profit["earned_money"] -= decimal.Decimal(i["bought"]) * decimal.Decimal(i["matecoin_price"])
            profit["matecoin_account"] += decimal.Decimal(i["bought"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
