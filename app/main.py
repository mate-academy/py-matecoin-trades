import decimal
import json


def calculate_profit(source_file_path: str) -> None:
    with open(source_file_path) as file:
        trades_data = json.load(file)

    total_profit = decimal.Decimal("0")
    matecoin_balance = decimal.Decimal("0")

    for trade in trades_data:
        trade_profit = decimal.Decimal("0")
        if trade["bought"]:
            trade_profit -= (
                decimal.Decimal(trade["bought"])
                * decimal.Decimal(trade["matecoin_price"])
            )
            matecoin_balance += decimal.Decimal(trade["bought"])
        if trade["sold"]:
            trade_profit += (
                decimal.Decimal(trade["sold"])
                * decimal.Decimal(trade["matecoin_price"])
            )
            matecoin_balance -= decimal.Decimal(trade["sold"])
        total_profit += decimal.Decimal(trade_profit)

    with open("profit.json", "w") as file:
        profit_result = {
            "earned_money": str(total_profit),
            "matecoin_account": str(matecoin_balance)
        }
        json.dump(profit_result, file, indent=2)
