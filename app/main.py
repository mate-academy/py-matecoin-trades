import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name) as data_in,
          open("profit.json", "w") as data_out):

        operations = json.load(data_in)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for each in operations:

            bought = each["bought"] if each["bought"] else "0"
            sold = each["sold"] if each["sold"] else "0"
            price = each["matecoin_price"]

            earned_money += (Decimal(sold) - Decimal(bought)) * Decimal(price)
            matecoin_account += (Decimal(bought) - Decimal(sold))

        profit = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}
        json.dump(profit, data_out, indent=2)
