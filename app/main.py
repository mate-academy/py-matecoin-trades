import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file:
        file_json = json.load(file)

    earned_money = matecoin_account = Decimal("0")

    for data in file_json:
        bought = data["bought"]
        sold = data["sold"]
        matecoin_price = data["matecoin_price"]

        if bought is not None:
            matecoin_account += Decimal(str(data["bought"]))
            earned_money -= Decimal(bought) * Decimal(matecoin_price)
        if sold is not None:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(matecoin_price)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    print(calculate_profit("app/trades.json"))
