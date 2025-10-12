import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    # Load trades data from the file
    with open(trades_file, "r") as file:
        trades: list[dict[str, Any]] = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Process each trade
    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        # Update Matecoin account and earned money
        matecoin_account += bought - sold
        earned_money += (sold - bought) * matecoin_price

    # Prepare the result
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Save the result to profit.json
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


# Example usage
# calculate_profit('trades.json')
