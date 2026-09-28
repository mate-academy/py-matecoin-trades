import decimal
import json


def calculate_profit(trades_file: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    with open(trades_file, "r") as f:
        trades = json.load(f)
        for trade in trades:
            if trade.get("bought"):
                bought_val = decimal.Decimal(trade["bought"])
                price_val = decimal.Decimal(trade["matecoin_price"])
                matecoin_account += bought_val
                earned_money -= bought_val * price_val

            if trade.get("sold"):
                sold_val = decimal.Decimal(trade["sold"])
                price_val = decimal.Decimal(trade["matecoin_price"])
                matecoin_account -= sold_val
                earned_money += sold_val * price_val

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
