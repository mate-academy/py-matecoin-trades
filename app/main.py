import json
from decimal import Decimal


RESULT_FILE_NAME = "profit.json"


def calculate_profit(report: str) -> None:
    coin_account = Decimal(0)
    profit = Decimal(0)

    with open(report, "r") as trade_report:
        trade_data = json.load(trade_report)

    for trade in trade_data:
        transaction_value = get_transaction_value(trade)
        coin_account += transaction_value
        profit -= transaction_value * Decimal(trade["matecoin_price"])

    profit_report_data = {"earned_money": str(profit),
                          "matecoin_account": str(coin_account)}

    with open(RESULT_FILE_NAME, "w") as profit_report:
        json.dump(profit_report_data, profit_report, indent=2)


def get_transaction_value(trade_data: dict) -> Decimal:
    bought = Decimal(trade_data["bought"])\
        if trade_data["bought"] is not None \
        else 0
    sold = Decimal(trade_data["sold"]) \
        if trade_data["sold"] is not None \
        else 0
    return bought - sold
