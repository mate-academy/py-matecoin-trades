import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as jsn_trade_file:
        trades_ls = json.load(jsn_trade_file)

    profit = {
        "earned_money": str(sum(
            [Decimal("-" + trade["bought"]) * Decimal(trade["matecoin_price"])
             if trade["bought"] else 0 for trade in trades_ls]
            + [Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                if trade["sold"] else 0 for trade in trades_ls]
        )),
        "matecoin_account": str(sum(
            [
                Decimal(trade["bought"]) if trade["bought"]
                else 0 for trade in trades_ls]
            + [
                Decimal("-" + trade["sold"]) if trade["sold"]
                else 0 for trade in trades_ls]
        ))
    }

    with open("profit.json", "w") as jsn_profit_file:
        json.dump(profit, jsn_profit_file, indent=2)
