import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_trade_info: str) -> None:
    total_bought = 0
    total_sold = 0
    matecoin_account = 0

    with open(file_trade_info, "r") as json_file:
        data = json.load(json_file)

    for item in data:
        bought = item.get("bought")
        if bought:
            bought = Decimal(bought)
            total_bought += (
                bought
                * Decimal(item.get("matecoin_price"))
            )
            matecoin_account += bought

        sold = item.get("sold")
        if sold:
            sold = Decimal(sold)
            total_sold += (
                sold
                * Decimal(item.get("matecoin_price"))
            )
            matecoin_account -= sold

    earned_money = total_sold - total_bought
    matecoin_account = {
        "earned_money":
            str(earned_money),
        "matecoin_account":
            str(matecoin_account)
    }

    profit_path = Path(file_trade_info).parent.parent / "profit.json"
    with open(profit_path, "w") as json_file:
        json.dump(matecoin_account, json_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
