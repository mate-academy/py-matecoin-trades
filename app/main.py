import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:

    with open(name_file) as f:
        trades_data = json.load(f)

    total_bought = Decimal(0)
    total_sold = Decimal(0)
    matecoin_account = Decimal(0)
    trade_result = {}

    for trade in trades_data:
        if trade["bought"]:
            total_bought += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"]:
            total_sold += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    trade_result["earned_money"] = str(total_sold - total_bought)
    trade_result["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as f:
        json.dump(trade_result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
