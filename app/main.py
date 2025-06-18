import json
from decimal import Decimal, ROUND_DOWN


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as original_file,
          open("../profit.json", "w") as new_file):
        content = json.load(original_file)

        crypto_bought_in_usd = sum(Decimal(element["bought"])
                                   * Decimal(element["matecoin_price"])
                                   for element in content
                                   if element["bought"] is not None)
        crypto_sold_in_usd = sum(Decimal(element["sold"])
                                 * Decimal(element["matecoin_price"])
                                 for element in content
                                 if element["sold"] is not None)
        earned_money = crypto_sold_in_usd - crypto_bought_in_usd

        crypto_qty_bought = sum(Decimal(element["bought"])
                                for element in content
                                if element["bought"] is not None)
        crypto_qty_sold = sum(Decimal(element["sold"]) for element in content
                              if element["sold"] is not None)
        crypto_account = crypto_qty_bought - crypto_qty_sold

        earned_money = earned_money.quantize(Decimal("0.0000001"),
                                             rounding=ROUND_DOWN)
        crypto_account = crypto_account.quantize(Decimal("0.00001"),
                                                 rounding=ROUND_DOWN)
        data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(crypto_account)
        }
        json.dump(data, new_file, indent=2)
