import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as json_file:
        data = json.load(json_file)
        profit = 0
        account = 0
        for operation in data:
            bought_items = Decimal(operation.get("bought") or "0")
            sold_items = Decimal(operation.get("sold") or "0")
            mate_coin_price = Decimal(operation.get("matecoin_price"))
            account_per_day = bought_items - sold_items
            profit_per_day = - account_per_day * mate_coin_price
            profit += profit_per_day
            account += account_per_day

    with open("profit.json", "w") as json_target:
        json.dump(
            {"earned_money": str(profit),
             "matecoin_account": str(account)}, json_target, indent=2
        )


if __name__ == "__main__":
    print(calculate_profit("app/trades.json"))
