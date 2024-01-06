import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        json_data = json.load(f)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for el in json_data:
        if el["bought"] is not None:
            matecoin_account += decimal.Decimal(el["bought"])
            earned_money -= decimal.Decimal(
                el["bought"]
            ) * decimal.Decimal(
                el["matecoin_price"]
            )
        if el["sold"] is not None:
            matecoin_account -= decimal.Decimal(el["sold"])
            earned_money += decimal.Decimal(
                el["sold"]
            ) * decimal.Decimal(
                el["matecoin_price"]
            )
    matecoin_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(matecoin_data, f, indent=2)
