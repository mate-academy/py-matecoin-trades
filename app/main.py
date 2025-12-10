import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    # Read and parse the trades JSON file
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    # Initialize variables for calculations
    total_spent = Decimal("0")  # Money spent buying coins
    total_earned = Decimal("0")  # Money earned selling coins
    matecoin_balance = Decimal("0")  # Current coin balance

    # Process each trade
    for trade in trades_data:
        matecoin_price = Decimal(str(trade["matecoin_price"]))

        # Handle bought coins
        if trade["bought"] is not None:
            bought_amount = Decimal(str(trade["bought"]))
            cost = bought_amount * matecoin_price
            total_spent += cost
            matecoin_balance += bought_amount

        # Handle sold coins
        if trade["sold"] is not None:
            sold_amount = Decimal(str(trade["sold"]))
            revenue = sold_amount * matecoin_price
            total_earned += revenue
            matecoin_balance -= sold_amount

    # Calculate net profit (earned - spent)
    earned_money = total_earned - total_spent

    # Prepare result data
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_balance)
    }

    # Save results to profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    # Calculate profit using the trades.json file
    calculate_profit("trades.json")
