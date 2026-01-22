import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        list_from_file = json.load(file)

    total_bought = 0
    total_sold = 0
    bought = 0
    sold = 0

    for transaction in list_from_file:
        if transaction["bought"] is not None:
            total_bought += \
                decimal.Decimal(transaction["bought"]) *\
                decimal.Decimal(transaction["matecoin_price"])
            bought += decimal.Decimal(transaction["bought"])
        if transaction["sold"] is not None:
            total_sold +=\
                decimal.Decimal(transaction["sold"]) *\
                decimal.Decimal(transaction["matecoin_price"])
            sold += decimal.Decimal(transaction["sold"])

    profit_dict = {"earned_money": str(total_sold - total_bought),
                   "matecoin_account": str(bought - sold)}

    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
