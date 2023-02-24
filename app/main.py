import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    profit = {"earned_money": Decimal("0"),
              "matecoin_account": Decimal("0")}

    with (open(name_of_file, "r") as data_file,
          open("profit.json", "w") as profit_file):

        data = json.load(data_file)

        for element in data:
            bought, sold, matecoin_price = element.values()
            if bought:
                profit["earned_money"] -= (Decimal(bought)
                                           * Decimal(matecoin_price))
                profit["matecoin_account"] += Decimal(bought)
            if sold:
                profit["earned_money"] += (Decimal(sold)
                                           * Decimal(matecoin_price))
                profit["matecoin_account"] -= Decimal(sold)

        json.dump({key: str(val) for key, val in profit.items()},
                  profit_file, indent=2)
