import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:

    with open(trades_file, "r") as file:
        trades = json.load(file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            bought = (
                Decimal(trade["bought"])if trade["bought"] else Decimal("0")
            )
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
            price = Decimal(trade["matecoin_price"])

            # Update matecoin account and earned money
            matecoin_account += bought
            matecoin_account -= sold
            earned_money -= bought * price
            earned_money += sold * price

    # Prepare profit data
    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Write profit.json
    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)


# Example usage
if __name__ == "__main__":
    pass
