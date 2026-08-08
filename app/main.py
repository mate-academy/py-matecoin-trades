import json
import decimal


def calculate_profit(trades_information: json) -> None:
    trade_result = {
        "matecoin_account": decimal.Decimal(0),
        "earned_money": decimal.Decimal(0)
    }
    with open(trades_information, "r") as f:
        trade_data = json.load(f)

        for trade in trade_data:
            if trade["bought"] is not None:
                trade_result["matecoin_account"] += \
                    decimal.Decimal(trade["bought"])
                trade_result["earned_money"] -= \
                    decimal.Decimal(trade["bought"]) *\
                    decimal.Decimal(trade["matecoin_price"])

            if trade["sold"] is not None:
                trade_result["matecoin_account"] -= \
                    decimal.Decimal(trade["sold"])
                trade_result["earned_money"] += \
                    decimal.Decimal(trade["sold"]) \
                    * decimal.Decimal(trade["matecoin_price"])

    with open("profit.json", "w") as f:
        trade_dump = {
            "earned_money": str(trade_result["earned_money"]),
            "matecoin_account": str(trade_result["matecoin_account"])
        }
        json.dump(trade_dump, f, indent=2)
