import json
from _decimal import Decimal


def calculate_profit(data_file_path: str) -> None:
    coins = Decimal(0)
    dollars = Decimal(0)
    with (open(data_file_path, "r") as data_source,
          open("profit.json", "w") as report):
        for obj in json.load(data_source):
            amount = ((Decimal(obj["bought"] or 0))
                      - (Decimal(obj["sold"] or 0)))
            dollars -= amount * Decimal(obj["matecoin_price"])
            coins += amount
        json.dump({
            "earned_money": str(dollars),
            "matecoin_account": str(coins)
        }, report, indent=2)
