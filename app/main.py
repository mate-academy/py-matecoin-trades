from decimal import Decimal
import json


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades = json.load(file)

    earn = Decimal("0")
    count = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        # Update earn and count
        earn -= bought * matecoin_price
        earn += sold * matecoin_price
        count += bought
        count -= sold

    # Create the result dictionary
    result = {
        "earned_money": str(earn),
        "matecoin_account": str(count)
    }

    # Write the result to profit.json
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

    print("Results written to profit.json")
