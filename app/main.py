import json
from decimal import Decimal


def calculate_profit(file_with_trade_info: str) -> None:
    with open(file_with_trade_info, "r") as trades_file:
        trades_data = json.load(trades_file)

    matecoin_account = 0
    earned_money = 0

    for trade_item in trades_data:
        if trade_item["bought"]:
            matecoin_account += Decimal(trade_item["bought"])
            earned_money \
                -= (Decimal(trade_item["bought"])
                    * Decimal(trade_item["matecoin_price"]))
        if trade_item["sold"]:
            matecoin_account -= Decimal(trade_item["sold"])
            earned_money \
                += (Decimal(trade_item["sold"])
                    * Decimal(trade_item["matecoin_price"]))

    with open("profit.json", "w") as profit_file:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            profit_file,
            indent=2
        )
