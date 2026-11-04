from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    profit: dict[str, str] = {
        "earned_money": "",
        "matecoin_account": ""
    }

    with open(file_name, "r", encoding="utf-8") as file:
        json_data = json.load(file)

        bought_count = Decimal("0")
        sold_count = Decimal("0")
        matecoin_count = Decimal("0")

        for trade in json_data:
            if trade["bought"] is not None:
                bought = Decimal(trade["bought"])
                price = Decimal(trade["matecoin_price"])

                bought_count += bought * price
                matecoin_count += bought

            if trade["sold"] is not None:
                sold = Decimal(trade["sold"])
                price = Decimal(trade["matecoin_price"])

                sold_count += sold * price
                matecoin_count -= sold

    profit["earned_money"] = str(sold_count - bought_count)
    profit["matecoin_account"] = str(matecoin_count)

    with open("profit.json", "w", encoding="utf-8") as file_out:
        json.dump(profit, file_out, indent=2)
