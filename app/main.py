import json
from decimal import Decimal


def calculate_profit(output_file: str = "profit.json") -> None:
    with open(output_file) as file_trades:
        user_trades_data = json.load(file_trades)

    user_money = Decimal("0")
    user_coin = Decimal("0")

    for trade in user_trades_data:
        if trade["bought"]:
            user_coin += Decimal(trade["bought"])
            user_money -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            user_coin -= Decimal(trade["sold"])
            user_money += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(user_money),
        "matecoin_account": str(user_coin)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
