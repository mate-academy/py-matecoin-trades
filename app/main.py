import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)

    bought_amount = decimal.Decimal("0")
    spend_money = decimal.Decimal("0")
    sold_amount = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")
    profit_dict = {}

    for transaction in data:
        if transaction["bought"]:
            bought_amount += decimal.Decimal(transaction["bought"])
            spend_money += (decimal.Decimal(transaction["bought"])
                            * decimal.Decimal(transaction["matecoin_price"]))

        if transaction["sold"]:
            sold_amount += decimal.Decimal(transaction["sold"])
            earned_money += (decimal.Decimal(transaction["sold"])
                             * decimal.Decimal(transaction["matecoin_price"]))

    profit_dict["earned_money"] = str(earned_money - spend_money)
    profit_dict["matecoin_account"] = str(bought_amount - sold_amount)

    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
