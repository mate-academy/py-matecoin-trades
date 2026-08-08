import json
import decimal


def calculate_profit(url: str) -> None:
    with open(url, "r") as f:
        trade_data = json.load(f)

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for transaction in trade_data:
        current_price = decimal.Decimal(transaction["matecoin_price"])
        current_plus = 0
        current_minus = 0
        if transaction["bought"] is not None:
            current_plus = decimal.Decimal(transaction["bought"])
        if transaction["sold"] is not None:
            current_minus = decimal.Decimal(transaction["sold"])

        profit["matecoin_account"] += current_plus - current_minus
        profit["earned_money"] -= \
            (current_plus - current_minus) * current_price

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
