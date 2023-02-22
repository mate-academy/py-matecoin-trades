import json
import decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name) as file:
        trade_data = json.load(file)
        print(trade_data)

    bought_amought = decimal.Decimal("0.0")
    sold_amought = decimal.Decimal("0.0")
    bought = decimal.Decimal("0.0")
    sold = decimal.Decimal("0.0")
    for operation in trade_data:
        if type(operation["bought"]) is str:
            temp_bought = decimal.Decimal(operation["bought"])
            temp_price = decimal.Decimal(operation["matecoin_price"])
            bought += temp_bought * temp_price
            bought_amought += temp_bought
        if type(operation["sold"]) is str:
            temp_sold = decimal.Decimal(operation["sold"])
            temp_price = decimal.Decimal(operation["matecoin_price"])
            sold += temp_sold * temp_price
            sold_amought += temp_sold

    final_value = sold - bought
    final_amought = bought_amought - sold_amought
    result_data = {
        "earned_money": str(final_value),
        "matecoin_account": str(final_amought)
    }

    with open("profit.json", "w") as file:
        json.dump(result_data, file, indent=2)
