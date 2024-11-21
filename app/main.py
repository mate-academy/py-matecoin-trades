import json
from decimal import Decimal
from typing import Optional


def calculate_profit(input_file: str) -> Optional[None]:
    """
    Calculate profit and Matecoin account balance from trades and
    save results to a JSON file.

    Args:
        input_file (str): Path to the JSON file containing trade data.

    Returns:
        None
    """
    output_file = "profit.json"

    # Read and parse the JSON file
    with open(input_file, "r") as file:
        trades = json.load(file)

    # Initialize Decimal values for calculations
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price
        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    # Prepare the result dictionary
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Write the result to the output JSON file
    with open(output_file, "w") as file:
        json.dump(result, file, indent=2)

    return None
