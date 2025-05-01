import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trade_info = json.load(file)

    for item in trade_info:
        for key, value in item.items():
            if value is None:
                item[key] = 0
            else:
                item[key] = decimal.Decimal(value)

    earned_money = sum(
        trade["sold"] * trade["matecoin_price"] for trade in trade_info
    )
    matecoin_account = (
        sum(trade["bought"] for trade in trade_info)
        - sum(trade["sold"] for trade in trade_info)
    )

    profit_dict = {
        "earned_money": float(earned_money),
        "matecoin_account": float(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file)
