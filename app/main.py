import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    profit_usd = Decimal("0")
    left_coin = Decimal("0")

    for trade in trades:
        bought = (
            Decimal("0") if trade.get("bought") is None
            else Decimal(trade.get("bought"))
        )
        sold = (
            Decimal("0") if trade.get("sold") is None
            else Decimal(trade.get("sold"))
        )
        price = Decimal(trade.get("matecoin_price"))

        left_coin += bought - sold
        profit_usd += (sold - bought) * price

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(profit_usd),
                "matecoin_account": str(left_coin),
            },
            file,
            indent=2,
        )


if __name__ == "__main__":
    calculate_profit("trades.json")