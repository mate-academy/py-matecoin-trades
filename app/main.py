import json
from decimal import Decimal


def calculate_profit(
        file_trades: str,
        file_profit: str = "profit.json"
) -> None:
    try:
        with open(file_trades) as trades, open(file_profit, "w") as profit:
            trades = json.load(trades)

            earned_money = Decimal("0")
            matecoin_account = Decimal("0")

            for trade in trades:
                sold = trade.get("sold")
                bought = trade.get("bought")
                matecoin_price = trade.get("matecoin_price")

                if bought:
                    earned_money -= Decimal(bought) * Decimal(matecoin_price)
                    matecoin_account += Decimal(bought)
                if sold:
                    earned_money += Decimal(sold) * Decimal(matecoin_price)
                    matecoin_account -= Decimal(sold)

            json.dump(
                {
                    "earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)
                },
                profit,
                indent=2
            )
    except (FileNotFoundError, PermissionError) as message:
        return message
