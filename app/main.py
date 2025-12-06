from decimal import Decimal
import json


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as json_trades:
        list_trades = json.load(json_trades)

    profit = Decimal("0")
    account = Decimal("0")
    for trade in list_trades:
        bought = Decimal(trade["bought"]) if (
            trade["bought"] is not None) else Decimal("0")
        sold = Decimal(trade["sold"]) if (
            trade["sold"] is not None) else Decimal("0")
        account += bought - sold

        profit += ((sold * Decimal(trade["matecoin_price"]))
                   - (bought * Decimal(trade["matecoin_price"])))
    dict_result = {
        "earned_money": str(profit),
        "matecoin_account": str(account)
    }
    with open("profit.json", "w") as json_file:
        json.dump(dict_result, json_file, indent=2)
