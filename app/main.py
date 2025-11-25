import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # read the trades from the json file
    with open(filename, "r") as f:
        trades = json.load(f)
    # initialize variables using Decimal for precision
    earned_money = Decimal("0")
    matecoin_acc = Decimal("0")

    # Process each trade
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            # buying coins = spending money
            bought_volume = Decimal(trade["bought"])
            cost = bought_volume * matecoin_price
            earned_money -= cost
            matecoin_acc += bought_volume

        if trade["sold"] is not None:
            # Selling coins - earning money
            sold_volume = Decimal(trade["sold"])
            revenue = sold_volume * matecoin_price
            earned_money += revenue
            matecoin_acc -= sold_volume
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_acc)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
