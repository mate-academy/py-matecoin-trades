from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        json_data = json.load(f)
    money = Decimal("0")
    coins = Decimal("0")
    for account in json_data:
        if account["bought"]:
            coins += Decimal(account["bought"])
            money -= Decimal(
                account["bought"]
            ) * Decimal(
                account["matecoin_price"]
            )
        if account["sold"]:
            coins -= Decimal(account["sold"])
            money += Decimal(
                account["sold"]
            ) * Decimal(
                account["matecoin_price"]
            )
    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
