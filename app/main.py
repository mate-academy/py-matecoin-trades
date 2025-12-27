import json
from decimal import Decimal


def calculate_profit(name_of_file: str = "trades.json") -> None:
    with open(f"{name_of_file}", "r") as f:
        file_data = json.load(f)
        earned_money = 0
        matecoin_account = Decimal("0")
        for data in file_data:
            if data["bought"]:
                earned_money -= (
                    Decimal(data["bought"]) * Decimal(data["matecoin_price"])
                )
                matecoin_account += Decimal(data["bought"])

            if data["sold"]:
                earned_money += (
                    Decimal(data["sold"]) * Decimal(data["matecoin_price"])
                )
                matecoin_account -= Decimal(data["sold"])

    def create_profit_file(profit: dict) -> None:
        with open("profit.json", "w") as profits:
            json.dump(profit, profits, ensure_ascii=False, indent=2)

    create_profit_file({"earned_money": str(earned_money),
                        "matecoin_account": str(matecoin_account)})


if __name__ == "__main__":
    calculate_profit()
