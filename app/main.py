import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as file:
        trade_info = json.load(file)

    trading_result = {"earned_money": Decimal("0"),
                      "matecoin_account": Decimal("0")}

    for items in trade_info:
        if items["bought"] is not None:
            bought = Decimal(items["bought"])
            matecoin_price = Decimal(items["matecoin_price"])
            trading_result["earned_money"] -= bought * matecoin_price
            trading_result["matecoin_account"] += bought

        if items["sold"] is not None:
            sold = Decimal(items["sold"])
            matecoin_price = Decimal(items["matecoin_price"])
            trading_result["earned_money"] += sold * matecoin_price
            trading_result["matecoin_account"] -= sold

    print(trading_result)

    result_for_json = {
        key: str(value) for key, value in trading_result.items()
    }

    with open("profit.json", "w") as new_file:
        json.dump(result_for_json, new_file, indent=2)
