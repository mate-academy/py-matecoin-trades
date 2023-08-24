import json
import decimal


def calculate_profit(f_name: str) -> None:
    with open(f_name, "r") as json_file:
        deserialized_file = json.load(json_file)

    json_data_to_write = {"earned_money": decimal.Decimal("0"),
                          "matecoin_account": decimal.Decimal("0")}

    for transaction in deserialized_file:

        bought_val = transaction["bought"]
        sold_val = transaction["sold"]
        price = decimal.Decimal(transaction["matecoin_price"])

        bought_amount = (decimal.Decimal("0")
                         if bought_val is None or bought_val == ""
                         else decimal.Decimal(bought_val))

        sold_amount = (decimal.Decimal("0")
                       if sold_val is None or sold_val == ""
                       else decimal.Decimal(sold_val))

        json_data_to_write["earned_money"] += (bought_amount
                                               - sold_amount) * price * -1
        json_data_to_write["matecoin_account"] += bought_amount - sold_amount

    json_data_to_write["earned_money"] = str(json_data_to_write
                                             ["earned_money"])
    json_data_to_write["matecoin_account"] = str(json_data_to_write
                                                 ["matecoin_account"])

    with open("profit.json", "w") as json_file:
        json.dump(json_data_to_write, json_file, indent=2)
