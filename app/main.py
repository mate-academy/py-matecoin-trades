import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as pickle_file,
          open("profit.json", "w") as profit_file):
        data = json.load(pickle_file)
        result = {
            "matecoin_account": Decimal("0"),
            "earned_money": Decimal("0")
        }
        for item in data:
            current_price = Decimal(item["matecoin_price"])
            if item.get("sold") is not None:
                sold_money = Decimal(item["sold"])
                result["matecoin_account"] -= sold_money
                result["earned_money"] += current_price * sold_money
            if item.get("bought") is not None:
                bought_money = Decimal(item["bought"])
                result["matecoin_account"] += + bought_money
                result["earned_money"] -= current_price * bought_money

        json.dump(
            {
                "earned_money": str(result["earned_money"]),
                "matecoin_account": str(result["matecoin_account"]),
            },
            profit_file,
            indent=2
        )


if __name__ == "__main__":
    calculate_profit("trades.json")
