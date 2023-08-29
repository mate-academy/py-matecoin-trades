import decimal
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(trades_file: str) -> None:
    try:
        with (
            open(trades_file) as trades_date,
            open(f"{BASE_DIR}/profit.json", "w") as profit_file,
        ):
            account_balance = decimal.Decimal("0.0")
            earned_money = decimal.Decimal("0.0")
            bought_sum = decimal.Decimal("0.0")
            sold_sum = decimal.Decimal("0.0")
            trades = json.load(trades_date)
            for transaction in trades:
                bought_amount = (
                    decimal.Decimal(transaction.get("bought"))
                    if transaction.get("bought")
                    else decimal.Decimal("0.0")
                )
                sold_amount = (
                    decimal.Decimal(transaction.get("sold"))
                    if transaction.get("sold")
                    else decimal.Decimal("0.0")
                )
                account_balance += bought_amount - sold_amount
                bought_sum += bought_amount * decimal.Decimal(
                    transaction.get("matecoin_price")
                )
                sold_sum += sold_amount * decimal.Decimal(
                    transaction.get("matecoin_price")
                )
            earned_money += sold_sum - bought_sum
            json.dump(
                {
                    "earned_money": str(earned_money),
                    "matecoin_account": str(account_balance),
                },
                profit_file,
                indent=2,
            )

    except FileNotFoundError:
        return
