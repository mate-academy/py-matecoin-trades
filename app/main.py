import json
from decimal import Decimal
import os


def calculate_profit(json_file: str, output_file: str = "profit.json") -> None:
    with open(json_file, 'r') as f:
        trades_data = json.load(f)

    total_bought = Decimal('0')
    total_sold = Decimal('0')
    money_spent = Decimal('0')
    money_earned = Decimal('0')

    for data in trades_data:
        price = Decimal(data["matecoin_price"])

        if data["bought"] is not None:
            bought = Decimal(data["bought"])
            total_bought += bought
            money_spent += bought * price

        if data["sold"] is not None:
            sold = Decimal(data["sold"])
            total_sold += sold
            money_earned += sold * price

    matecoin_account = total_bought - total_sold
    earned_money = money_earned - money_spent

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    output_path = os.path.abspath(output_file)

    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
