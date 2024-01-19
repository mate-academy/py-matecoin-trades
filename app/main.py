import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades_data = json.load(file)

    # Initialize variables
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    # Process each trade
    for trade in trades_data:
        if trade.get("bought") is not None:

            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            cost = bought_volume * matecoin_price
            earned_money -= cost
            matecoin_account += bought_volume
        if trade.get("sold") is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            revenue = sold_volume * matecoin_price
            earned_money += revenue
            matecoin_account -= sold_volume

    # Prepare the result
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Save the result to profit.json
    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
