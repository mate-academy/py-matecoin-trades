import json
import os

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        file_content = json.load(f)
    decimal_profit = Decimal("0.00000")
    matecoin_account = Decimal("0.00000")
    for content in file_content:
        dec_bought = Decimal(content.get("bought", "0.00000") or "0.00000")
        dec_sold = Decimal(content.get("sold", "0.00000") or "0.00000")
        dec_mateacc = Decimal(content.get("matecoin_price", "0.00000"))
        if dec_bought > Decimal("0.00000"):
            decimal_profit -= (dec_bought * dec_mateacc)
            matecoin_account += dec_bought
        if dec_sold > Decimal("0.00000"):
            decimal_profit += (dec_sold * dec_mateacc)
            matecoin_account -= dec_sold
    finish_content = {
        "earned_money": str(decimal_profit),
        "matecoin_account": str(matecoin_account)
    }
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    result_path = parent_dir + "/profit.json"

    os.makedirs(os.path.dirname(result_path), exist_ok=True)

    with open(result_path, "w") as f2:
        json.dump(finish_content, f2, indent=2)
