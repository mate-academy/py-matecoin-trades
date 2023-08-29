import json
from decimal import Decimal


def calculate_profit(file_name):
    # Load JSON data from the specified file
    with open(file_name, "r") as file:
        trades = json.load(file)

    # Initialize variables
    total_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Process each trade
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        # Handle buying
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            total_money -= bought_volume * matecoin_price
            matecoin_account += bought_volume

        # Handle selling
        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            total_money += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    # Prepare profit data
    profit_data = {
        "earned_money": str(total_money),
        "matecoin_account": str(matecoin_account)
    }

    # Save data to profit.json
    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=4)
