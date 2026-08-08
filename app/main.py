from decimal import Decimal
import json


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as file, open("profit.json", "w") as pro:
        trades_info = json.load(file)
        result = {
            "earned_money": Decimal(),
            "matecoin_account": Decimal()
        }
        sold = Decimal()
        buy = Decimal()
        for key in trades_info:
            if key["sold"] is not None:
                result["matecoin_account"] -= Decimal(key["sold"])
                sold += Decimal(key["sold"]) * Decimal(key["matecoin_price"])
            if key["bought"] is not None:
                result["matecoin_account"] += Decimal(key["bought"])
                buy += Decimal(key["bought"]) * Decimal(key["matecoin_price"])
        result["earned_money"] = sold - buy

        analysis_dict = {x: str(y) for x, y in result.items()}
        json.dump(analysis_dict, pro, indent=2)
