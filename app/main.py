from decimal import Decimal
import json


def calculate_profit(input_file: str) -> None:
    try:
        with open(input_file) as file:
            transactions = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return None

    total_bought = 0
    total_sold = 0
    earned = 0

    for transaction in transactions:
        bought = Decimal(
            transaction["bought"]
        ) if transaction["bought"] is not None else Decimal("0")
        sold = Decimal(
            transaction["sold"]
        ) if transaction["sold"] is not None else Decimal("0")
        total_bought += bought
        total_sold += sold
        earned += Decimal(transaction["matecoin_price"]) * sold
        earned -= Decimal(transaction["matecoin_price"]) * bought

    account = total_bought - total_sold

    profit = {"earned_money": str(earned), "matecoin_account": str(account)}
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
