"""Calculate profit and balances from matecoin trades."""

import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    """
    Calculate profit and account balance from matecoin trades.

    Args:
        file_name: Path to the JSON file containing trade records.
    """
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    trade_data = load_config(file_name)

    for trade in trade_data:
        if trade["bought"] is not None:
            payment = coin_to_usd(trade["bought"], trade["matecoin_price"])
            earned_money -= payment
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            income = coin_to_usd(trade["sold"], trade["matecoin_price"])
            earned_money += income
            matecoin_account -= Decimal(trade["sold"])
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(profit, f, indent=2)


def coin_to_usd(
    matecoin_amount: str,
    matecoin_price: str
) -> Decimal:
    """
    Convert matecoin amount to USD value.

    Args:
        matecoin_amount: The amount of matecoin as a string.
        matecoin_price: The price of matecoin in USD as a string.

    Returns:
        The USD value as a Decimal.
    """
    return Decimal(matecoin_amount) * Decimal(matecoin_price)


def load_config(trades_path: str) -> list:
    """
    Load trade records from a JSON file.

    Args:
        trades_path: Path to the JSON file containing trade records.

    Returns:
        A list of trade records.
    """
    with open(trades_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config
