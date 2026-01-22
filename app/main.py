import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}", "r") as file:
        operations = json.load(file)

    bought = 0
    sold = 0
    matecoin_account = 0

    for operation in operations:
        if operation["bought"] is not None:
            bought += (decimal.Decimal(operation.get("bought"))
                       * decimal.Decimal(operation.get("matecoin_price")))
            matecoin_account += decimal.Decimal(operation.get("bought"))
        if operation["sold"] is not None:
            sold += (decimal.Decimal(operation.get("sold"))
                     * decimal.Decimal(operation.get("matecoin_price")))
            matecoin_account -= decimal.Decimal(operation.get("sold"))

    profit_dict = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
