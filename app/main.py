import json
from decimal import Decimal


def calculate_profit(trade_json: json) -> None:
    result = {
        "earned_money": "0",
        "matecoin_account": "0"
    }
    with open(trade_json) as trade_file:
        file_transaction = json.load(trade_file)

    for trans in file_transaction:
        if trans["sold"] is None:
            trans["sold"] = "0"
        if trans["bought"] is None:
            trans["bought"] = "0"
        result["earned_money"] = str(
            Decimal(result["earned_money"])
            - Decimal(trans["bought"])
            * Decimal(trans["matecoin_price"])
            + Decimal(trans["sold"])
            * Decimal(trans["matecoin_price"])
        )
        result["matecoin_account"] = str(
            Decimal(result["matecoin_account"])
            + Decimal(trans["bought"])
            - Decimal(trans["sold"])
        )

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
