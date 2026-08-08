import json
import decimal


def calculate_profit(filename: str) -> None:
    result = {
        "earned_money": decimal.Decimal(0),
        "matecoin_account": decimal.Decimal(0)
    }

    with open(filename) as file_in:
        transactions = json.load(file_in)
        for record in transactions:
            if record["bought"] is not None:
                bought = decimal.Decimal(record["bought"])
            else:
                bought = 0
            if record["sold"] is not None:
                sold = decimal.Decimal(record["sold"])
            else:
                sold = 0
            if record["matecoin_price"] is not None:
                price = decimal.Decimal(record["matecoin_price"])
            else:
                price = 0

            result["matecoin_account"] += bought - sold
            result["earned_money"] += price * (sold - bought)

    with (open("profit.json", "w")) as file_out:
        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])
        json.dump(result, file_out, indent=2)

# calculate_profit("trades.json")
