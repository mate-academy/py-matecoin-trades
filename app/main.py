import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with (open(name, "r") as file, open("profit.json", "w") as file_result):
        trading_data = json.load(file)
        money_earned = Decimal("0")
        matecoin_account = Decimal("0")
        for trading_day in trading_data:
            bought = (
                Decimal(trading_day["bought"])
                if trading_day["bought"] is not None
                else Decimal("0")
            )
            sold = (
                Decimal(trading_day["sold"])
                if trading_day["sold"] is not None
                else Decimal("0")
            )
            matecoin_account += bought - sold
            money_earned += ((sold - bought)
                             * Decimal(trading_day["matecoin_price"]))
        profit_dict = {
            "earned_money": str(money_earned),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(profit_dict, file_result, indent=2)
