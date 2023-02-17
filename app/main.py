import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        bought = sold = bought_amount = sold_amount = decimal.Decimal("0")

        for item in data:
            if item["bought"] is not None:
                bought_amount += (
                    decimal.Decimal(item["bought"])
                    * decimal.Decimal(item["matecoin_price"])
                )
                bought += decimal.Decimal(item["bought"])
            if item["sold"] is not None:
                sold_amount += (
                    decimal.Decimal(item["sold"])
                    * decimal.Decimal(item["matecoin_price"]))
                sold += decimal.Decimal(item["sold"])
        result = {"earned_money": str(sold_amount - bought_amount),
                  "matecoin_account": str(bought - sold)}

    with open("profit.json", "w") as file_out:
        json.dump(result, file_out, indent=2)
