import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as traders:
        trade_data = json.load(traders)

    trade_results = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for data in trade_data:
        if data["bought"] is None:
            data["bought"] = 0
        if data["sold"] is None:
            data["sold"] = 0
        trade_delta = \
            decimal.Decimal(data["bought"]) - decimal.Decimal(data["sold"])
        trade_results["matecoin_account"] += trade_delta
        trade_results["earned_money"] += \
            trade_delta * decimal.Decimal(data["matecoin_price"])

    trade_results["matecoin_account"] = str(trade_results["matecoin_account"])
    trade_results["earned_money"] = str(-trade_results["earned_money"])

    with open("profit.json", "w") as profit:
        json.dump(trade_results, profit, indent=2)
