from decimal import Decimal
import json
from typing import List, Dict, Optional


def calculate_profit(trades_file: str) -> None:
    # Load trades from the JSON file
    with open(trades_file, "r", encoding="utf-8") as file:
        trades: List[Dict[str, Optional[str]]] = json.load(file)

    # Initialize variables with Decimal
    total_spent: Decimal = Decimal("0")  # Money spent buying Matecoin
    total_earned: Decimal = Decimal("0")  # Money earned selling Matecoin
    matecoin_balance: Decimal = Decimal("0")  # Current Matecoin balance

    # Process each trade
    for trade in trades:
        price: Decimal = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount: Decimal = Decimal(trade["bought"])
            total_spent += bought_amount * price
            matecoin_balance += bought_amount

        if trade["sold"] is not None:
            sold_amount: Decimal = Decimal(trade["sold"])
            total_earned += sold_amount * price
            matecoin_balance -= sold_amount

    # Calculate profit (earned - spent)
    profit: Decimal = total_earned - total_spent

    # Prepare result dictionary with string values
    result: Dict[str, str] = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_balance)
    }

    # Save result to profit.json with indentation
    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)

    # Return None as required by the test
    return None


# Example usage
if __name__ == "__main__":
    calculate_profit("trades.json")
