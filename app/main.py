import os
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_name}'.")
        return

    matecoin_account = 0
    earned_money = 0

    for operation in data:
        if operation.get("bought"):
            matecoin_account += Decimal(operation["bought"])
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation.get("matecoin_price", 0)))

        if operation.get("sold"):
            matecoin_account -= Decimal(operation["sold"])
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation.get("matecoin_price", 0)))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.join(script_directory, "..")
    output_file_path = os.path.join(parent_directory, "profit.json")

    try:
        with open(output_file_path, "w") as file:
            json.dump(result, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing to 'profit.json': {e}")
        return
