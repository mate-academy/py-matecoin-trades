import decimal
import json


def calculate_profit(sales_data_file: str) -> None:
    with open(sales_data_file, "r") as file:
        sales_data = json.load(file)
    total_sold = 0
    total_bought = 0
    total_coins = 0
    for _ in sales_data:
        total_sold += (decimal.Decimal(_["matecoin_price"])
                       * decimal.Decimal(_["sold"])) if _["sold"] else 0
        total_coins -= decimal.Decimal(_["sold"]) if _["sold"] else 0
        total_bought += (decimal.Decimal(_["matecoin_price"])
                         * decimal.Decimal(_["bought"])) if _["bought"] else 0
        total_coins += decimal.Decimal(_["bought"]) if _["bought"] else 0

    earned = total_sold - total_bought
    result = {
        "earned_money": str(earned),
        "matecoin_account": str(total_coins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
