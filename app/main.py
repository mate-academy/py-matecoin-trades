import json
from decimal import Decimal


def calculate_profit(trade_info: str) -> None:
    with open(trade_info, "r") as trades_file:
        trades_data = json.load(trades_file)

    crypto_coin = Decimal("0")
    crypto_money = Decimal("0")

    for trade in trades_data:
        if trade["bought"] is not None:
            crypto_coin += Decimal(trade["bought"])
            crypto_money -= (
                Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
            )
        if trade["sold"] is not None:
            crypto_coin -= Decimal(trade["sold"])
            crypto_money += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
            )

    profit = {
        "earned_money": str(crypto_money),
        "matecoin_account": str(crypto_coin)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
