import json
import decimal


def calculate_profit(file_name):
    with open(file_name, "r") as file_in:
        data = json.load(file_in)

    sell = 0
    buy = 0
    currency = 0
    for transaction in data:
        if transaction["bought"] is not None:
            currency += decimal.Decimal(transaction["bought"])
            buy += decimal.Decimal(transaction["bought"]) *\
                decimal.Decimal(transaction["matecoin_price"])
        if transaction["sold"] is not None:
            currency -= decimal.Decimal(transaction["sold"])
            sell += decimal.Decimal(transaction["sold"]) *\
                decimal.Decimal(transaction["matecoin_price"])
    profit = str(sell - buy)
    currency = str(currency)

    d_res = {
        "earned_money": profit,
        "matecoin_account": currency
    }

    with open("profit.json", "w") as file_out:
        json.dump(d_res, file_out, indent=2)
