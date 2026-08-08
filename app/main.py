import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as f:
        transactions = json.load(f)
        bought = 0
        sold = 0
        am_bold = 0
        am_sold = 0
        for el in transactions:
            bought += 0 \
                if el["bought"] is None \
                else Decimal(el["bought"]) * Decimal(el["matecoin_price"])
            sold += 0 \
                if el["sold"] is None \
                else Decimal(el["sold"]) * Decimal(el["matecoin_price"])
            am_bold += 0 \
                if el["bought"] is None \
                else Decimal(el["bought"])
            am_sold += 0 \
                if el["sold"] is None \
                else Decimal(el["sold"])
    print(f"bought: {am_bold}; sold: {am_sold}")
    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(sold - bought),
                   "matecoin_account": str(am_bold - am_sold)}, f, indent=2)
