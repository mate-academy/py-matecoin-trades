import json
from decimal import Decimal


def calculate_profit(file: str):
    with open(file) as trade_info:
        data_trade = json.load(trade_info)
    bought = Decimal("0")
    sold = Decimal("0")
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for deal in data_trade:
        if deal["bought"]:
            bought += Decimal(deal["bought"]) * Decimal(deal["matecoin_price"])
            profit["matecoin_account"] += Decimal(deal["bought"])
        if deal["sold"]:
            sold += Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
            profit["matecoin_account"] -= Decimal(deal["sold"])
    profit["earned_money"] = str(bought - sold)
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as profit_report:
        json.dump(profit, profit_report, indent=2)
