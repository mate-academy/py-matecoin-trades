import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(filename: str) -> None:
    """
    Calculates profit and coin balance from
    trades and saves them to profit.json.

    Parameters:
        filename: Name of the file containing trade data.
    Returns:
        None
    """
    root_dir = Path(__file__).resolve().parent.parent
    profit_file_path = root_dir / "profit.json"

    with open(filename, "r") as file:
        trades = json.load(file)

    total_earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        price = Decimal(trade["matecoin_price"])

        if bought:
            matecoin_account += Decimal(bought)
            total_earned_money -= price * Decimal(bought)

        if sold:
            matecoin_account -= Decimal(sold)
            total_earned_money += price * Decimal(sold)

    profit_data = {
        "earned_money": str(total_earned_money.normalize()),
        "matecoin_account": str(matecoin_account.normalize())
    }

    with open(profit_file_path, "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)

    print("The profit.json file was successfully created.")
