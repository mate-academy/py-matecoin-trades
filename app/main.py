import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f, open("profit.json", "w") as in_file:
        date_file = json.load(f)
        count = Decimal("0")
        buy = Decimal("0")
        for i in date_file:
            if i["bought"]:
                count -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                buy += Decimal(i["bought"])
            if i["sold"]:
                count += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                buy -= Decimal(i["sold"])
        profit = {"earned_money": str(count),
                  "matecoin_account": str(buy)
                  }
        json.dump(profit, in_file, indent=2)
