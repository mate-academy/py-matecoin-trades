from decimal import Decimal
import json


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as json_file:
        trade_data = json.load(json_file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trade_data:
        bought = Decimal(trade["bought"]) if (trade["bought"]
                                              is not None) else Decimal("0")
        sold = Decimal(trade["sold"]) if (trade["sold"]
                                          is not None) else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought > 0:
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold > 0:
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
