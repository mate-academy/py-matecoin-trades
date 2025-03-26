import logging
import os
import json
from decimal import Decimal

logging.basicConfig(level=logging.DEBUG)

PROFIT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "profit.json")


def calculate_profit(trades_file):
    # Ensure the directory exists where the profit.json file should be saved
    os.makedirs(os.path.dirname(PROFIT), exist_ok=True)

    logging.debug(f"Saving profit to {PROFIT}")

    total_bought = Decimal(0)
    total_sold = Decimal(0)
    matecoin_account = Decimal(0)

    with open(trades_file, 'r') as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            total_bought += Decimal(bought) * matecoin_price
            matecoin_account += Decimal(bought)

        if sold is not None:
            total_sold += Decimal(sold) * matecoin_price
            matecoin_account -= Decimal(sold)

    earned_money = total_sold - total_bought

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Write the result to profit.json
    logging.debug(f"Writing data to {PROFIT}: {profit_data}")

    with open(PROFIT, 'w') as file:
        json.dump(profit_data, file, indent=2)
