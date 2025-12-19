import json
from pathlib import Path
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    base_dir = Path(__file__).resolve().parent.parent
    new_file = f"{base_dir}/profit.json"

    try:
        with open(file_name, "r") as file:
            coins_list = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return

    list_for_profit = (
        [
            ((Decimal(transaction.get("bought", Decimal("0")))
             if transaction.get("bought") is not None
             else Decimal("0")) - (Decimal(transaction.get("sold"))
             if transaction.get("sold", Decimal("0")) is not None
             else Decimal("0")),
             Decimal(transaction["matecoin_price"]))
            for transaction in coins_list
        ]
    )

    matecoin_account = sum(matecoin[0]
                           for matecoin in list_for_profit)
    earned_money = sum(-matecoin[0] * matecoin[1]
                       for matecoin in list_for_profit)

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open(new_file, "w") as file:
        json.dump(result, file, indent=2)
