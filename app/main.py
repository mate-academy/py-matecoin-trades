import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    bought = Decimal("0")
    sold = Decimal("0")
    money_from_sale = Decimal("0")
    money_purchases = Decimal("0")
    with open(trades_file) as file:
        trades_data = json.load(file)

    for trades in trades_data:
        if trades["bought"] is None:
            trades["bought"] = 0
        if trades["sold"] is None:
            trades["sold"] = 0
    for trades in trades_data:
        sold += Decimal(trades["sold"])
        bought += Decimal(trades["bought"])
        money_from_sale += (Decimal(trades["sold"])
                            * Decimal(trades["matecoin_price"]))
        money_purchases += (Decimal(trades["bought"])
                            * Decimal(trades["matecoin_price"]))

    profit = {
        "earned_money": str(money_from_sale - money_purchases),
        "matecoin_account": str(bought - sold)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
